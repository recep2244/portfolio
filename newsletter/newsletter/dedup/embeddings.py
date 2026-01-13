"""Embedding generation and caching for semantic deduplication."""

import hashlib
import os
import time
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np

# Lazy load sentence-transformers to avoid import overhead
_model = None
_model_name = "all-MiniLM-L6-v2"

DEFAULT_CACHE_DIR = Path(__file__).parent.parent / ".embeddings_cache"
CACHE_MAX_AGE_DAYS = 30


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
    """Generate a hash for caching."""
    return hashlib.sha256(text.lower().strip().encode()).hexdigest()[:16]


def _get_cache_path(text_hash: str, cache_dir: Path) -> Path:
    """Get cache file path for an embedding."""
    return cache_dir / f"{text_hash}.npy"


def _load_cached_embedding(text_hash: str, cache_dir: Path) -> Optional[np.ndarray]:
    """Load embedding from cache if it exists and is fresh."""
    cache_path = _get_cache_path(text_hash, cache_dir)
    if not cache_path.exists():
        return None

    # Check age
    age_days = (time.time() - cache_path.stat().st_mtime) / 86400
    if age_days > CACHE_MAX_AGE_DAYS:
        cache_path.unlink(missing_ok=True)
        return None

    try:
        return np.load(cache_path)
    except Exception:
        return None


def _save_embedding(embedding: np.ndarray, text_hash: str, cache_dir: Path):
    """Save embedding to cache."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = _get_cache_path(text_hash, cache_dir)
    try:
        np.save(cache_path, embedding)
    except Exception:
        pass  # Cache failures are not critical


def get_embedding(
    title: str,
    abstract: str = "",
    cache_dir: Optional[Path] = None,
    use_cache: bool = True,
) -> np.ndarray:
    """
    Generate embedding for a paper's title and abstract.

    Args:
        title: Paper title
        abstract: Paper abstract (first 200 chars used)
        cache_dir: Directory for embedding cache
        use_cache: Whether to use caching

    Returns:
        Normalized embedding vector
    """
    # Combine title and truncated abstract
    text = f"{title.strip()}. {abstract[:200].strip()}" if abstract else title.strip()
    text_hash = _text_hash(text)

    cache_dir = cache_dir or DEFAULT_CACHE_DIR

    # Try cache first
    if use_cache:
        cached = _load_cached_embedding(text_hash, cache_dir)
        if cached is not None:
            return cached

    # Generate embedding
    model = _get_model()
    embedding = model.encode(text, normalize_embeddings=True)

    # Cache it
    if use_cache:
        _save_embedding(embedding, text_hash, cache_dir)

    return embedding


def get_embeddings_batch(
    texts: List[Tuple[str, str]],
    cache_dir: Optional[Path] = None,
    use_cache: bool = True,
    show_progress: bool = False,
) -> np.ndarray:
    """
    Generate embeddings for multiple papers.

    Args:
        texts: List of (title, abstract) tuples
        cache_dir: Directory for embedding cache
        use_cache: Whether to use caching
        show_progress: Print progress indicator

    Returns:
        Array of normalized embeddings (N x embedding_dim)
    """
    cache_dir = cache_dir or DEFAULT_CACHE_DIR

    # Check cache for each text
    embeddings = []
    uncached_indices = []
    uncached_texts = []

    for i, (title, abstract) in enumerate(texts):
        text = f"{title.strip()}. {abstract[:200].strip()}" if abstract else title.strip()
        text_hash = _text_hash(text)

        if use_cache:
            cached = _load_cached_embedding(text_hash, cache_dir)
            if cached is not None:
                embeddings.append((i, cached))
                continue

        uncached_indices.append(i)
        uncached_texts.append(text)

    # Generate uncached embeddings in batch
    if uncached_texts:
        if show_progress:
            print(f"Generating embeddings for {len(uncached_texts)} papers...")

        model = _get_model()
        new_embeddings = model.encode(
            uncached_texts,
            normalize_embeddings=True,
            show_progress_bar=show_progress,
        )

        # Cache new embeddings
        if use_cache:
            for text, embedding in zip(uncached_texts, new_embeddings):
                text_hash = _text_hash(text)
                _save_embedding(embedding, text_hash, cache_dir)

        # Add to results
        for idx, embedding in zip(uncached_indices, new_embeddings):
            embeddings.append((idx, embedding))

    # Sort by original index and extract embeddings
    embeddings.sort(key=lambda x: x[0])
    return np.array([e[1] for e in embeddings])


def clean_old_cache(cache_dir: Optional[Path] = None, max_age_days: int = CACHE_MAX_AGE_DAYS):
    """Remove cache files older than max_age_days."""
    cache_dir = cache_dir or DEFAULT_CACHE_DIR
    if not cache_dir.exists():
        return 0

    removed = 0
    cutoff = time.time() - (max_age_days * 86400)

    for cache_file in cache_dir.glob("*.npy"):
        try:
            if cache_file.stat().st_mtime < cutoff:
                cache_file.unlink()
                removed += 1
        except Exception:
            pass

    return removed


def warmup_model():
    """Pre-load the model to avoid first-call latency."""
    _get_model()
