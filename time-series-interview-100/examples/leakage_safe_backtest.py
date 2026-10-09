import numpy as np
import pandas as pd

from ts_interview.baselines import seasonal_naive
from ts_interview.metrics import mase
from ts_interview.validation import expanding_window_splits

rng = np.random.default_rng(0)
n = 500
t = np.arange(n)
y = 100 + 0.03*t + 8*np.sin(2*np.pi*t/7) + rng.normal(0, 2, n)
df = pd.DataFrame({"y": y})

scores=[]
for tr, va in expanding_window_splits(len(df), min_train_size=280, horizon=28, step=28):
    y_train=df.iloc[tr]["y"].to_numpy()
    y_true=df.iloc[va]["y"].to_numpy()
    pred=seasonal_naive(y_train, horizon=len(va), seasonality=7)
    scores.append(mase(y_true,pred,y_train,seasonality=7))
print("fold MASE:", [round(x,3) for x in scores])
print("mean MASE:", round(float(np.mean(scores)),3))
