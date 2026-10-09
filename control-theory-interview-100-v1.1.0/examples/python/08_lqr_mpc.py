"""Q071-Q080: continuous LQR gain; MPC extension is left as an exercise."""
import numpy as np
from scipy.linalg import solve_continuous_are
A=np.array([[0,1],[0,0]],float)
B=np.array([[0],[1]],float)
Q=np.diag([10,1]); R=np.array([[1.]])
P=solve_continuous_are(A,B,Q,R)
K=np.linalg.solve(R,B.T@P)
print('K=',K)
# Add box constraints and a finite horizon with cvxpy to turn this into MPC.
