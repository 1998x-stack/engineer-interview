from __future__ import annotations

import numpy as np

def expanding_window_splits(n_samples: int, min_train_size: int, horizon: int, step: int = 1):
    """Yield chronological train/validation positional indices.

    Validation is strictly after training. No preprocessing is performed here; callers
    should fit transformations inside each fold.
    """
    if min_train_size <= 0 or horizon <= 0 or step <= 0:
        raise ValueError("min_train_size, horizon and step must be positive")
    cutoff = min_train_size
    while cutoff + horizon <= n_samples:
        yield np.arange(0, cutoff), np.arange(cutoff, cutoff + horizon)
        cutoff += step
