from __future__ import annotations

import numpy as np

def seasonal_naive(history, horizon: int, seasonality: int = 1):
    y = np.asarray(history, dtype=float)
    if len(y) < seasonality: raise ValueError("insufficient history")
    idx = np.arange(horizon) % seasonality
    return y[-seasonality:][idx]
