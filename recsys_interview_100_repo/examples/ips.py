"""IPS / clipped IPS illustration."""
from typing import Iterable


def ips_loss(losses: Iterable[float], propensities: Iterable[float], clip: float = 20.0) -> float:
    vals = []
    for loss, p in zip(losses, propensities):
        w = min(1.0 / max(p, 1e-8), clip)
        vals.append(w * loss)
    return sum(vals) / len(vals)

if __name__ == "__main__":
    print(ips_loss([0.2, 0.5, 0.1], [0.5, 0.1, 0.02]))
