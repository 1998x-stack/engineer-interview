# Newsvendor-style mapping from asymmetric cost to target quantile.

def optimal_quantile(c_under: float, c_over: float) -> float:
    return c_under / (c_under + c_over)

print(optimal_quantile(c_under=5, c_over=1))
