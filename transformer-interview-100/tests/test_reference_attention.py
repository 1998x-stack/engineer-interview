import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import torch
from examples.reference_attention import ReferenceMHA, causal_mask

def test_shape_and_finite():
    m=ReferenceMHA(32,4).eval();x=torch.randn(2,7,32)
    y=m(x,causal_mask(7))
    assert y.shape==(2,7,32)
    assert torch.isfinite(y).all()

def test_causal_prefix_invariance():
    torch.manual_seed(0)
    m=ReferenceMHA(32,4).eval()
    x1=torch.randn(1,8,32);x2=x1.clone();x2[:,5:]=torch.randn_like(x2[:,5:])
    mask=causal_mask(8)
    y1=m(x1,mask);y2=m(x2,mask)
    torch.testing.assert_close(y1[:,:5],y2[:,:5],atol=1e-5,rtol=1e-5)
