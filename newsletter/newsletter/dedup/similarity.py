#!/usr/bin/env python3
"""Semantic similarity detection and deduplication for papers."""

import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional, Set, Tuple

import numpy as np

from .embeddings import get_embeddings_batch, warmup_model


@dataclass
class Paper:
    """Paper data structure (matches generate_issue.py Paper)."""
    title: str
    summary: str
    link: str
    published: datetime
    source: str


class UnionFind:
    """Union-Find data structure for grouping duplicates."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

    def get_groups(self) -> List[Set[int]]:
        groups = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in groups:
                groups[root] = set()
            groups[root].add(i)
        return [g for g in groups.values() if len(g) > 1]


def cosine_similarity_matrix(embeddings: np.ndarray) -> np.ndarray:
    """
    Compute pairwise cosine similarity matrix.

    Since embeddings are normalized, cosine similarity = dot product.
    """
    return np.dot(embeddings, embeddings.T)


def find_semantic_duplicates(
    papers: List[Any],
    threshold: float = 0.80,
    cache_dir: Optional[Path] = None,
    verbose: bool = False,
) -> Tuple[List[Set[int]], np.ndarray]:
    """
    Find groups of semantically similar papers.

    Args:
        papers: List of Paper objects (or any object with title and summary attributes)
        threshold: Cosine similarity threshold (0.80 = 80% similar)
        cache_dir: Directory for embedding cache
        verbose: Print progress information

    Returns:
        Tuple of (duplicate groups, similarity matrix)
        Each group is a set of paper indices that are duplicates of each other
    """
    if len(papers) < 2:
        return [], np.array([])

    # Extract texts
    texts = []
    for p in papers:
        title = getattr(p, 'title', '') or (p.get('title', '') if isinstance(p, dict) else '')
        summary = getattr(p, 'summary', '') or (p.get('summary', '') if isinstance(p, dict) else '')
        texts.append((title, summary))

    if verbose:
        print(f"Computing embeddings for {len(texts)} papers...")

    # Get embeddings
    embeddings = get_embeddings_batch(texts, cache_dir=cache_dir, show_progress=verbose)

    # Compute similarity matrix
    sim_matrix = cosine_similarity_matrix(embeddings)

    # Find pairs above threshold
    uf = UnionFind(len(papers))
    duplicate_pairs = []

    for i in range(len(papers)):
        for j in range(i + 1, len(papers)):
            if sim_matrix[i, j] >= threshold:
                uf.union(i, j)
                duplicate_pairs.append((i, j, sim_matrix[i, j]))

    groups = uf.get_groups()

    if verbose and groups:
        print(f"Found {len(groups)} duplicate groups:")
        for group in groups:
            titles = [texts[i][0][:50] for i in group]
            print(f"  Group: {titles}")

    return groups, sim_matrix


def semantic_dedupe_papers(
    papers: List[Any],
    threshold: float = 0.80,
    score_fn: Optional[callable] = None,
    cache_dir: Optional[Path] = None,
    verbose: bool = False,
) -> Tuple[List[Any], List[Set[int]]]:
    """
    Remove semantic duplicates from a list of papers.

    Keeps the highest-scored paper from each duplicate group.

    Args:
        papers: List of Paper objects
        threshold: Cosine similarity threshold for duplicates
        score_fn: Function to score papers (higher = better). If None, keeps first in group.
        cache_dir: Directory for embedding cache
        verbose: Print progress information

    Returns:
        Tuple of (deduplicated papers list, duplicate groups that were merged)
    """
    if len(papers) < 2:
        return papers, []

    groups, _ = find_semantic_duplicates(
        papers,
        threshold=threshold,
        cache_dir=cache_dir,
        verbose=verbose,
    )

    if not groups:
        return papers, []

    # Collect indices to remove
    to_remove = set()

    for group in groups:
        group_list = list(group)

        if score_fn:
            # Keep highest scored paper
            scores = [(idx, score_fn(papers[idx])) for idx in group_list]
            scores.sort(key=lambda x: x[1], reverse=True)
            keep_idx = scores[0][0]
        else:
            # Keep first paper (earliest in list, usually highest scored already)
            keep_idx = min(group_list)

        # Mark others for removal
        for idx in group_list:
            if idx != keep_idx:
                to_remove.add(idx)

    # Build deduplicated list
    deduplicated = [p for i, p in enumerate(papers) if i not in to_remove]

    if verbose:
        print(f"Removed {len(to_remove)} semantic duplicates, {len(deduplicated)} papers remain")

    return deduplicated, groups


def test_similarity():
    """Test semantic similarity detection with example papers."""
    test_papers = [
        Paper(
            title="AlphaFold2 predicts protein structures with high accuracy",
            summary="A deep learning method for protein structure prediction that achieves atomic accuracy.",
            link="https://example.com/1",
            published=datetime.now(),
            source="test",
        ),
        Paper(
            title="Accurate protein structure prediction using AlphaFold2",
            summary="Deep learning achieves breakthrough in predicting protein 3D structures.",
            link="https://example.com/2",
            published=datetime.now(),
            source="test",
        ),
        Paper(
            title="RFdiffusion enables de novo protein design",
            summary="A generative model for designing novel protein structures from scratch.",
            link="https://example.com/3",
            published=datetime.now(),
            source="test",
        ),
        Paper(
            title="Novel generative approach for de novo protein design",
            summary="Using diffusion models to create new protein structures computationally.",
            link="https://example.com/4",
            published=datetime.now(),
            source="test",
        ),
        Paper(
            title="CRISPR gene editing advances in clinical trials",
            summary="Clinical applications of CRISPR technology show promising results.",
            link="https://example.com/5",
            published=datetime.now(),
            source="test",
        ),
    ]

    print("Testing semantic similarity detection...")
    print(f"Threshold: 0.80\n")

    warmup_model()

    groups, sim_matrix = find_semantic_duplicates(test_papers, threshold=0.80, verbose=True)

    print(f"\nSimilarity matrix:")
    for i, p1 in enumerate(test_papers):
        print(f"\n{i}. {p1.title[:40]}...")
        for j, p2 in enumerate(test_papers):
            if i != j:
                print(f"   vs {j}: {sim_matrix[i, j]:.3f}")

    print(f"\n\nRunning deduplication...")
    deduplicated, merged = semantic_dedupe_papers(test_papers, threshold=0.80, verbose=True)

    print(f"\nKept papers:")
    for p in deduplicated:
        print(f"  - {p.title[:60]}...")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Semantic deduplication for papers")
    parser.add_argument("--test", action="store_true", help="Run test with example papers")
    parser.add_argument("--threshold", type=float, default=0.80, help="Similarity threshold")
    args = parser.parse_args()

    if args.test:
        test_similarity()
    else:
        print("Use --test to run example similarity detection")
        print("Or import semantic_dedupe_papers() in your code")


if __name__ == "__main__":
    main()
