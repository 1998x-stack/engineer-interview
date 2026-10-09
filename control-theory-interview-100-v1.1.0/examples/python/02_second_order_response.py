"""Q011-Q020: second-order step responses."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t=np.linspace(0,10,2000)
for zeta in [0.2,0.5,0.707,1.0]:
    wn=2.0
    sys=signal.TransferFunction([wn**2],[1,2*zeta*wn,wn**2])
    tout,y=signal.step(sys,T=t)
    plt.plot(tout,y,label=f"zeta={zeta}")
plt.axhline(1,ls='--',lw=0.8)
plt.legend(); plt.xlabel('t [s]'); plt.ylabel('y'); plt.grid(True); plt.show()
