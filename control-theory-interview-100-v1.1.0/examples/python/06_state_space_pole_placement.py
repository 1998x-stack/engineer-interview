"""Q051-Q060: state feedback pole placement."""
import numpy as np
from scipy.signal import place_poles
A=np.array([[0,1],[-2,-0.4]])
B=np.array([[0],[1]])
K=place_poles(A,B,[-2,-3]).gain_matrix
print('K=',K)
print('closed-loop eig=',np.linalg.eigvals(A-B@K))
