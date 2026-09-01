"""Factorization Machine second-order term in O(nd)."""
import numpy as np


def fm_second_order(x: np.ndarray, V: np.ndarray) -> float:
    vx = V * x[:, None]
    return float(0.5 * np.sum(np.sum(vx, axis=0) ** 2 - np.sum(vx ** 2, axis=0)))

if __name__ == "__main__":
    x = np.array([1.0, 0.0, 2.0])
    V = np.array([[0.1, 0.2], [0.3, -0.2], [0.4, 0.1]])
    print(fm_second_order(x, V))
