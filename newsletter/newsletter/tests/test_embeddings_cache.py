"""Tests for the consolidated SQLite embedding cache.

These exercise the cache store directly with synthetic vectors, so the
sentence-transformers model is never loaded.
"""
import time

import numpy as np
import pytest

from dedup import embeddings as emb


def _vec(seed):
    rng = np.random.default_rng(seed)
    v = rng.standard_normal(8).astype(np.float32)
    return v / np.linalg.norm(v)


def test_put_get_roundtrip(tmp_path):
    v = _vec(1)
    emb._cache_put("abc123", v, tmp_path)
    got = emb._cache_get("abc123", tmp_path)
    assert got is not None
    assert np.allclose(got, v)


def test_missing_key_returns_none(tmp_path):
    assert emb._cache_get("does-not-exist", tmp_path) is None


def test_put_many_roundtrip(tmp_path):
    items = [(f"h{i}", _vec(i)) for i in range(5)]
    emb._cache_put_many(items, tmp_path)
    for h, v in items:
        assert np.allclose(emb._cache_get(h, tmp_path), v)


def test_batch_uses_cache_without_model(tmp_path, monkeypatch):
    # Pre-populate the cache for two texts, then ensure the batch call returns
    # them as hits and never touches the model.
    texts = [("Protein folding", ""), ("Drug discovery", "")]
    hashes = [emb._text_hash(emb._prepare_text(t, a)) for t, a in texts]
    vecs = [_vec(10), _vec(11)]
    emb._cache_put_many(list(zip(hashes, vecs)), tmp_path)

    def _boom():
        raise AssertionError("model should not be loaded on a full cache hit")

    monkeypatch.setattr(emb, "_get_model", _boom)

    out = emb.get_embeddings_batch(texts, cache_dir=tmp_path)
    assert out.shape == (2, 8)
    assert np.allclose(out[0], vecs[0])
    assert np.allclose(out[1], vecs[1])


def test_legacy_npy_fallback_and_migration(tmp_path):
    # Write a legacy .npy and confirm it is read, then migrated into the DB.
    v = _vec(2)
    tmp_path.mkdir(parents=True, exist_ok=True)
    np.save(tmp_path / "legacyhash.npy", v)

    got = emb._cache_get("legacyhash", tmp_path)
    assert np.allclose(got, v)

    # After access it should be in the DB (remove the file, still resolvable).
    (tmp_path / "legacyhash.npy").unlink()
    assert np.allclose(emb._cache_get("legacyhash", tmp_path), v)


def test_age_eviction(tmp_path):
    v = _vec(3)
    emb._cache_put("stale", v, tmp_path)
    # Backdate the row beyond the max age.
    conn = emb._connect(tmp_path)
    old = time.time() - (emb.CACHE_MAX_AGE_DAYS + 1) * 86400
    conn.execute("UPDATE embeddings SET created = ? WHERE hash = ?", (old, "stale"))
    conn.commit()
    conn.close()
    assert emb._cache_get("stale", tmp_path) is None


def test_migrate_legacy_npy(tmp_path):
    tmp_path.mkdir(parents=True, exist_ok=True)
    for i in range(3):
        np.save(tmp_path / f"m{i}.npy", _vec(i))
    imported, deleted = emb.migrate_legacy_npy(tmp_path, delete=True)
    assert imported == 3
    assert deleted == 3
    # All resolvable from the DB now.
    for i in range(3):
        assert emb._cache_get(f"m{i}", tmp_path) is not None
