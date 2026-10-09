import pandas as pd
from ts_interview.features import add_safe_lag_rolling_features

df = pd.DataFrame({
    "series_id": ["A"]*8,
    "y": [10,11,12,11,13,15,14,16],
})
print(add_safe_lag_rolling_features(df, "series_id", "y", lags=(1,2), windows=(3,)))
