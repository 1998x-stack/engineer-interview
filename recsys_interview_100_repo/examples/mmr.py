"""Greedy Maximal Marginal Relevance reranking."""
from collections.abc import Callable


def mmr(items, relevance: dict, similarity: Callable, k: int, lam: float = 0.8):
    selected = []
    remaining = list(items)
    while remaining and len(selected) < k:
        def score(i):
            redundancy = max((similarity(i, j) for j in selected), default=0.0)
            return lam * relevance[i] - (1 - lam) * redundancy
        best = max(remaining, key=score)
        selected.append(best)
        remaining.remove(best)
    return selected
