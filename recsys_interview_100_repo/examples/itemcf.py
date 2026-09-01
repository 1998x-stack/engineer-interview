"""Minimal ItemCF example for interview study."""
from collections import defaultdict
from math import sqrt


def item_similarity(user_items: dict[str, set[str]]) -> dict[str, dict[str, float]]:
    item_users: dict[str, set[str]] = defaultdict(set)
    for user, items in user_items.items():
        for item in items:
            item_users[item].add(user)
    out: dict[str, dict[str, float]] = defaultdict(dict)
    items = list(item_users)
    for a in items:
        for b in items:
            if a == b:
                continue
            ua, ub = item_users[a], item_users[b]
            out[a][b] = len(ua & ub) / sqrt(len(ua) * len(ub))
    return dict(out)

if __name__ == "__main__":
    data = {"u1": {"a", "b"}, "u2": {"a", "c"}, "u3": {"a", "b", "c"}}
    print(item_similarity(data))
