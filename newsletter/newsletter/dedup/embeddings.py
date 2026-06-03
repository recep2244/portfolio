"""Embedding generation and caching for semantic deduplication.

Embeddings are cached in a single consolidated SQLite store
(``.embeddings_cache/embeddings.db``) keyed by a content hash. Earlier versions
wrote one ``.npy`` file per paper, which produced thousands of tiny files; those
legacy files are still read transparently (and migrated into the DB on access),
so upgrading is seamless. Use ``migrate_legacy_npy()`` to bulk-import and clean
them up.

The public API — ``get_embedding``, ``get_embeddings_batch``, ``clean_old_cache``,
``warmup_model`` — is unchanged.
"""

import hashlib
import io
import sqlite3
import time
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np

# Lazy load sentence-transformers to avoid import overhead
_model = None
_model_name = "all-MiniLM-L6-v2"

DEFAULT_CACHE_DIR = Path(__file__).parent.parent / ".embeddings_cache"
CACHE_MAX_AGE_DAYS = 30
_DB_NAME = "embeddings.db"

# Track which DB paths have had their schema initialised (per process).
_initialised: set = set()


def _get_model():
    """Lazy load the sentence transformer model."""
    global _model
    if _model is None:
        try:
            from sentence_transformers import SentenceTransformer
            _model = SentenceTransformer(_model_name)
        except ImportError:
            raise ImportError(
                "sentence-transformers not installed. Run: pip install sentence-transformers"
            )
    return _model


def _text_hash(text: str) -> str:
    """Generate a stable hash for caching."""
    return hashlib.sha256(text.lower().strip().encode()).hexdigest()[:16]


def _prepare_text(title: str, abstract: str = "") -> str:
    """Build the text used for embedding (title + truncated abstract)."""
    return f"{title.strip()}. {abstract[:200].strip()}" if abstract else title.strip()


# ──────────────────────────────────────────────────────────────────────────────
# SQLite-backed cache store
# ──────────────────────────────────────────────────────────────────────────────

def _db_path(cache_dir: Path) -> Path:
    return cache_dir / _DB_NAME


def _connect(cache_dir: Path) -> sqlite3.Connection:
    """Open a connection to the cache DB, creating the schema once per path.

    A fresh short-lived connection is used per operation/batch, which keeps the
    store safe to use across threads (e.g. the Flask curation server).
    """
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = _db_path(cache_dir)
    conn = sqlite3.connect(path, timeout=30)
    key = str(path)
    if key not in _initialised:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute(
            "CREATE TABLE IF NOT EXISTS embeddings ("
            "  hash TEXT PRIMARY KEY,"
            "  vec  BLOB NOT NULL,"
            "  created REAL NOT NULL"
            ")"
        )
        conn.commit()
        _initialised.add(key)
    return conn


def _serialize(emb: np.ndarray) -> bytes:
    """Serialise an embedding to bytes using the self-describing .npy format."""
    buf = io.BytesIO()
    np.save(buf, emb, allow_pickle=False)
    return buf.getvalue()


def _deserialize(blob: bytes) -> np.ndarray:
    return np.load(io.BytesIO(blob), allow_pickle=False)


def _legacy_path(text_hash: str, cache_dir: Path) -> Path:
    return cache_dir / f"{text_hash}.npy"


def _cache_get(text_hash: str, cache_dir: Path) -> Optional[np.ndarray]:
    """Return a fresh cached embedding, or None.

    Looks in the SQLite store first; falls back to a legacy ``.npy`` file
    (migrating it into the DB) so older caches keep working.
    """
    cutoff = time.time() - CACHE_MAX_AGE_DAYS * 86400
    try:
        conn = _connect(cache_dir)
        try:
            row = conn.execute(
                "SELECT vec, created FROM embeddings WHERE hash = ?", (text_hash,)
            ).fetchone()
            if row is not None:
                vec, created = row
                if created < cutoff:
                    conn.execute("DELETE FROM embeddings WHERE hash = ?", (text_hash,))
                    conn.commit()
                    return None
                return _deserialize(vec)
        finally:
            conn.close()
    except Exception:
        pass  # fall through to legacy / miss

    # Legacy single-file fallback (+ lazy migration).
    legacy = _legacy_path(text_hash, cache_dir)
    if legacy.exists():
        age_days = (time.time() - legacy.stat().st_mtime) / 86400
        if age_days > CACHE_MAX_AGE_DAYS:
            legacy.unlink(missing_ok=True)
            return None
        try:
            emb = np.load(legacy)
            _cache_put(text_hash, emb, cache_dir)  # migrate forward
            return emb
        except Exception:
            return None
    return None


def _cache_put(text_hash: str, emb: np.ndarray, cache_dir: Path) -> None:
    """Store one embedding (best-effort; cache failures are not critical)."""
    try:
        conn = _connect(cache_dir)
        try:
            conn.execute(
                "INSERT OR REPLACE INTO embeddings (hash, vec, created) VALUES (?, ?, ?)",
                (text_hash, _serialize(emb), time.time()),
            )
            conn.commit()
        finally:
            conn.close()
    except Exception:
        pass


def _cache_put_many(items: List[Tuple[str, np.ndarray]], cache_dir: Path) -> None:
    """Store many embeddings in a single transaction."""
    if not items:
        return
    try:
        now = time.time()
        conn = _connect(cache_dir)
        try:
            conn.executemany(
                "INSERT OR REPLACE INTO embeddings (hash, vec, created) VALUES (?, ?, ?)",
                [(h, _serialize(e), now) for h, e in items],
            )
            conn.commit()
        finally:
            conn.close()
    except Exception:
        pass


# ──────────────────────────────────────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────────────────────────────────────

def get_embedding(
    title: str,
    abstract: str = "",
    cache_dir: Optional[Path] = None,
    use_cache: bool = True,
) -> np.ndarray:
    """Generate a normalized embedding for a paper's title and abstract."""
    cache_dir = cache_dir or DEFAULT_CACHE_DIR
    text = _prepare_text(title, abstract)
    text_hash = _text_hash(text)

    if use_cache:
        cached = _cache_get(text_hash, cache_dir)
        if cached is not None:
            return cached

    model = _get_model()
    embedding = model.encode(text, normalize_embeddings=True)

    if use_cache:
        _cache_put(text_hash, embedding, cache_dir)

    return embedding


def get_embeddings_batch(
    texts: List[Tuple[str, str]],
    cache_dir: Optional[Path] = None,
    use_cache: bool = True,
    show_progress: bool = False,
) -> np.ndarray:
    """Generate normalized embeddings for many (title, abstract) pairs.

    Returns an array of shape (N, embedding_dim) in the input order.
    """
    cache_dir = cache_dir or DEFAULT_CACHE_DIR

    embeddings: List[Tuple[int, np.ndarray]] = []
    uncached_indices: List[int] = []
    uncached_texts: List[str] = []
    uncached_hashes: List[str] = []

    for i, (title, abstract) in enumerate(texts):
        text = _prepare_text(title, abstract)
        text_hash = _text_hash(text)

        if use_cache:
            cached = _cache_get(text_hash, cache_dir)
            if cached is not None:
                embeddings.append((i, cached))
                continue

        uncached_indices.append(i)
        uncached_texts.append(text)
        uncached_hashes.append(text_hash)

    if uncached_texts:
        if show_progress:
            print(f"Generating embeddings for {len(uncached_texts)} papers...")

        model = _get_model()
        new_embeddings = model.encode(
            uncached_texts,
            normalize_embeddings=True,
            show_progress_bar=show_progress,
        )

        if use_cache:
            _cache_put_many(list(zip(uncached_hashes, new_embeddings)), cache_dir)

        for idx, embedding in zip(uncached_indices, new_embeddings):
            embeddings.append((idx, embedding))

    embeddings.sort(key=lambda x: x[0])
    return np.array([e[1] for e in embeddings])


def clean_old_cache(cache_dir: Optional[Path] = None, max_age_days: int = CACHE_MAX_AGE_DAYS) -> int:
    """Remove cache entries (DB rows and legacy files) older than max_age_days."""
    cache_dir = cache_dir or DEFAULT_CACHE_DIR
    if not cache_dir.exists():
        return 0

    removed = 0
    cutoff = time.time() - (max_age_days * 86400)

    # DB rows
    try:
        conn = _connect(cache_dir)
        try:
            cur = conn.execute("DELETE FROM embeddings WHERE created < ?", (cutoff,))
            removed += cur.rowcount or 0
            conn.commit()
            conn.execute("VACUUM")
        finally:
            conn.close()
    except Exception:
        pass

    # Legacy files
    for cache_file in cache_dir.glob("*.npy"):
        try:
            if cache_file.stat().st_mtime < cutoff:
                cache_file.unlink()
                removed += 1
        except Exception:
            pass

    return removed


def migrate_legacy_npy(cache_dir: Optional[Path] = None, delete: bool = False) -> Tuple[int, int]:
    """Bulk-import legacy per-paper ``.npy`` files into the SQLite store.

    Args:
        cache_dir: cache directory (defaults to DEFAULT_CACHE_DIR)
        delete: if True, remove each ``.npy`` after it is imported

    Returns:
        (imported, deleted) counts
    """
    cache_dir = cache_dir or DEFAULT_CACHE_DIR
    if not cache_dir.exists():
        return (0, 0)

    imported = deleted = 0
    batch: List[Tuple[str, np.ndarray]] = []
    files = list(cache_dir.glob("*.npy"))

    for f in files:
        try:
            emb = np.load(f)
        except Exception:
            continue
        batch.append((f.stem, emb))
        if len(batch) >= 512:
            _cache_put_many(batch, cache_dir)
            imported += len(batch)
            batch = []

    if batch:
        _cache_put_many(batch, cache_dir)
        imported += len(batch)

    if delete:
        for f in files:
            try:
                f.unlink()
                deleted += 1
            except Exception:
                pass

    return (imported, deleted)


def warmup_model():
    """Pre-load the model to avoid first-call latency."""
    _get_model()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Embedding cache maintenance")
    parser.add_argument("--migrate", action="store_true", help="Import legacy .npy files into the DB")
    parser.add_argument("--delete-legacy", action="store_true", help="Delete .npy files after import")
    parser.add_argument("--clean", action="store_true", help="Remove entries older than max age")
    args = parser.parse_args()

    if args.migrate:
        imp, dele = migrate_legacy_npy(delete=args.delete_legacy)
        print(f"Migrated {imp} legacy embeddings into DB; deleted {dele} .npy files.")
    if args.clean:
        print(f"Removed {clean_old_cache()} stale cache entries.")
    if not (args.migrate or args.clean):
        parser.print_help()
