"""Q031-Q040: root-locus example (python-control)."""
import control as ct
import matplotlib.pyplot as plt
G=ct.tf([1],[1,3,2,0])
ct.root_locus(G,grid=True)
plt.show()
