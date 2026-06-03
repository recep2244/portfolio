"""Deterministic unit tests for the semantic-dedup core.

These tests inject precomputed embeddings, so they never load the
sentence-transformers model (no torch download / GPU needed) and run in
milliseconds. Only numpy is required.
"""
import numpy as np
import pytest

from dedup.similarity import (
    UnionFind,
    cosine_similarity_matrix,
    find_semantic_duplicates,
    semantic_dedupe_papers,
)


def _paper(title, summary=""):
    return {"title": title, "summary": summary}


# Three unit vectors: 0 and 1 identical (cos=1), 2 orthogonal (cos=0).
DUP_EMBEDDINGS = np.array(
    [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=np.float32
)
DUP_PAPERS = [
    _paper("AlphaFold2 predicts protein structure"),
    _paper("Accurate protein structure prediction with AlphaFold2"),
    _paper("CRISPR gene editing in clinical trials"),
]


class TestUnionFind:
    def test_union_groups_transitively(self):
        uf = UnionFind(4)
        uf.union(0, 1)
        uf.union(1, 2)
        groups = uf.get_groups()
        assert len(groups) == 1
        assert groups[0] == {0, 1, 2}

    def test_singletons_excluded(self):
        uf = UnionFind(3)  # no unions
        assert uf.get_groups() == []


class TestCosineMatrix:
    def test_diagonal_is_one(self):
        m = cosine_similarity_matrix(DUP_EMBEDDINGS)
        assert np.allclose(np.diag(m), 1.0)

    def test_orthogonal_is_zero(self):
        m = cosine_similarity_matrix(DUP_EMBEDDINGS)
        assert m[0, 2] == pytest.approx(0.0, abs=1e-6)

    def test_identical_vectors_are_one(self):
        m = cosine_similarity_matrix(DUP_EMBEDDINGS)
        assert m[0, 1] == pytest.approx(1.0, abs=1e-6)


class TestFindSemanticDuplicates:
    def test_groups_identical_pair(self):
        groups, _ = find_semantic_duplicates(
            DUP_PAPERS, threshold=0.80, embeddings=DUP_EMBEDDINGS
        )
        assert groups == [{0, 1}]

    def test_high_threshold_finds_nothing(self):
        # cos(0,1)=1.0 but raise threshold above it -> no dupes
        groups, _ = find_semantic_duplicates(
            DUP_PAPERS, threshold=1.01, embeddings=DUP_EMBEDDINGS
        )
        assert groups == []

    def test_fewer_than_two_papers(self):
        groups, matrix = find_semantic_duplicates([_paper("solo")], threshold=0.8)
        assert groups == []
        assert matrix.size == 0


class TestSemanticDedupe:
    def test_keeps_highest_scored(self):
        # score paper index 1 highest -> it survives, index 0 dropped
        scores = {id(DUP_PAPERS[0]): 1.0, id(DUP_PAPERS[1]): 9.0, id(DUP_PAPERS[2]): 5.0}
        kept, groups = semantic_dedupe_papers(
            DUP_PAPERS,
            threshold=0.80,
            score_fn=lambda p: scores[id(p)],
            embeddings=DUP_EMBEDDINGS,
        )
        assert len(kept) == 2
        assert DUP_PAPERS[1] in kept  # higher-scored survivor
        assert DUP_PAPERS[0] not in kept
        assert groups == [{0, 1}]

    def test_no_duplicates_returns_all(self):
        distinct = np.eye(3, dtype=np.float32)  # mutually orthogonal
        kept, groups = semantic_dedupe_papers(
            DUP_PAPERS, threshold=0.80, embeddings=distinct
        )
        assert len(kept) == 3
        assert groups == []
