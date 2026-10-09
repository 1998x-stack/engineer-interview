"""Q001-Q010: feedback sensitivity demo."""
import numpy as np

def sensitivity(L):
    return 1/(1+L)

for L in [0.1, 1, 10, 100]:
    print(f"L={L:>5}: S={sensitivity(L):.4f}, T={1-sensitivity(L):.4f}")
