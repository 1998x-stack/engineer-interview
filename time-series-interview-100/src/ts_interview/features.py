from __future__ import annotations

import pandas as pd

def add_safe_lag_rolling_features(df: pd.DataFrame, group_col: str, target_col: str, lags=(1,7,14), windows=(7,28)) -> pd.DataFrame:
    """Create leakage-safe historical features using shift before rolling."""
    out = df.copy()
    g = out.groupby(group_col, sort=False)[target_col]
    for lag in lags:
        out[f"lag_{lag}"] = g.shift(lag)
    for window in windows:
        out[f"rolling_mean_{window}"] = g.transform(lambda s: s.shift(1).rolling(window, min_periods=1).mean())
        out[f"rolling_std_{window}"] = g.transform(lambda s: s.shift(1).rolling(window, min_periods=2).std())
    return out
