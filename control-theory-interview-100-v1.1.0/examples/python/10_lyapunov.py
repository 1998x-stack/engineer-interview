"""Q091-Q100: continuous Lyapunov equation."""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
A=np.array([[-1,2],[-3,-4]],float)
Q=np.eye(2)
# scipy solves A P + P A^T = Qarg; use -Q
P=solve_continuous_lyapunov(A,-Q)
print('eig(P)=',np.linalg.eigvalsh(P))
print('residual=',A@P+P@A.T+Q)
