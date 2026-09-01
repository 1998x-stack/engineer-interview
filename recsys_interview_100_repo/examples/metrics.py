"""Small ranking metric helpers."""
from math import log2


def dcg(rels: list[float], k: int) -> float:
    return sum((2**r - 1) / log2(i + 2) for i, r in enumerate(rels[:k]))


def ndcg(rels: list[float], k: int) -> float:
    best = sorted(rels, reverse=True)
    denom = dcg(best, k)
    return dcg(rels, k) / denom if denom else 0.0


def recall_at_k(recommended: list[str], positives: set[str], k: int) -> float:
    return len(set(recommended[:k]) & positives) / len(positives) if positives else 0.0

if __name__ == "__main__":
    print(ndcg([3, 0, 2, 1], 4))
