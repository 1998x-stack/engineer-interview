import numpy as np
from ts_interview.metrics import mase, rmsse, pinball_loss, interval_coverage

def test_metrics_smoke():
    train=np.arange(1,11,dtype=float)
    true=np.array([11.,12.])
    pred=np.array([10.,12.])
    assert mase(true,pred,train,1) >= 0
    assert rmsse(true,pred,train,1) >= 0
    assert pinball_loss(true,pred,0.5) >= 0
    assert interval_coverage(true,[10,11],[12,13]) == 1.0
