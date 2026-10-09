from __future__ import annotations

import numpy as np

def _a(x): return np.asarray(x, dtype=float)

def mase(y_true, y_pred, y_train, seasonality: int = 1) -> float:
    y_true, y_pred, y_train = _a(y_true), _a(y_pred), _a(y_train)
    if seasonality < 1 or len(y_train) <= seasonality:
        raise ValueError("invalid seasonality or insufficient training history")
    scale = np.mean(np.abs(y_train[seasonality:] - y_train[:-seasonality]))
    return float(np.mean(np.abs(y_true-y_pred)) / (scale + 1e-12))

def rmsse(y_true, y_pred, y_train, seasonality: int = 1) -> float:
    y_true, y_pred, y_train = _a(y_true), _a(y_pred), _a(y_train)
    scale = np.mean((y_train[seasonality:] - y_train[:-seasonality])**2)
    return float(np.sqrt(np.mean((y_true-y_pred)**2) / (scale + 1e-12)))

def pinball_loss(y_true, q_pred, quantile: float) -> float:
    if not 0 < quantile < 1: raise ValueError("quantile must be in (0, 1)")
    e = _a(y_true) - _a(q_pred)
    return float(np.mean(np.maximum(quantile*e, (quantile-1)*e)))

def interval_coverage(y_true, lower, upper) -> float:
    y, lo, hi = _a(y_true), _a(lower), _a(upper)
    return float(np.mean((y >= lo) & (y <= hi)))

def mean_interval_width(lower, upper) -> float:
    return float(np.mean(_a(upper)-_a(lower)))
