#probability density plot
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import exp
from numpy import pi
number = np.arange(0,5,1)
for n in number:
  radius = []
  wavefunction =[]
  for r in np.arange(0,1,0.002):
    y =(np.sqrt(2/1)*np.sin(n*np.pi*r))
    R=y*y
    radius.append(r)
    wavefunction.append(R)
  plt.plot(radius,wavefunction, label=f'n={n}')
plt.title("probability density plot")
plt.xlabel("r")
plt.ylabel("probability")
plt.legend(loc='upper right')
plt.show()
