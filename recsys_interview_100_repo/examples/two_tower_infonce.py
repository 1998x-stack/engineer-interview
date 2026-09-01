"""NumPy-only InfoNCE sketch for a two-tower retriever."""
import numpy as np


def l2norm(x: np.ndarray) -> np.ndarray:
    return x / np.maximum(np.linalg.norm(x, axis=-1, keepdims=True), 1e-12)


def infonce_loss(user_vecs: np.ndarray, item_vecs: np.ndarray, temperature: float = 0.1) -> float:
    u, v = l2norm(user_vecs), l2norm(item_vecs)
    logits = (u @ v.T) / temperature
    logits -= logits.max(axis=1, keepdims=True)
    log_probs = logits - np.log(np.exp(logits).sum(axis=1, keepdims=True))
    return float(-np.diag(log_probs).mean())

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    print(infonce_loss(rng.normal(size=(8, 16)), rng.normal(size=(8, 16))))
