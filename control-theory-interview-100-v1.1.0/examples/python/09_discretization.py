"""Q081-Q090: exact ZOH discretization."""
import numpy as np
from scipy.signal import cont2discrete
A=np.array([[0,1],[-4,-1]],float)
B=np.array([[0],[1]],float)
C=np.array([[1,0]],float); D=np.array([[0]],float)
for Ts in [0.1,0.02]:
    Ad,Bd,_,_,_=cont2discrete((A,B,C,D),Ts,method='zoh')
    print('Ts=',Ts,'eig(Ad)=',np.linalg.eigvals(Ad))
