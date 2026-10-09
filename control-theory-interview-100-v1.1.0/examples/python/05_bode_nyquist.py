"""Q041-Q050: Bode margins and Nyquist."""
import control as ct
import matplotlib.pyplot as plt
G=ct.tf([10],[1,3,2,0])
gm,pm,wcg,wcp=ct.margin(G)
print('GM=',gm,'PM=',pm,'wcg=',wcg,'wcp=',wcp)
ct.bode_plot(G,dB=True,grid=True)
plt.show()
