#Radial factor plot for hydrogenic orbitals
import math
import numpy as np
from numpy import pi
from numpy import arange
import matplotlib.pyplot as plt

a0 = 0.529177
Z = 1
orbitals = ['1s', '2s', '2p', '3s']
r = np.arange(0, 30, 0.1)

for orb in orbitals:
    R = []
    r_vals = []
    for c in arange(0, 30, 0.1):
        if orb == '1s':
            n = 2 * (Z/a0)**(3/2) * (np.exp(-(Z*c)/a0))
        elif orb == '2s':
            n = (1/(2*math.sqrt(2))) * (Z/a0)**(3/2) * (2 - (Z*c)/a0) * (np.exp(-(Z*c)/(2*a0)))
        elif orb == '2p':
            n = (1/(2*math.sqrt(6))) * (Z/a0)**(3/2) * ((Z*c)/a0) * (np.exp(-(Z*c)/(2*a0)))
        elif orb == '3s':
            n = (2/(81*math.sqrt(3))) * (Z/a0)**(3/2) * (27 - 18*(Z*c)/a0 + 2*((Z*c)/a0)**2) * (np.exp(-(Z*c)/(3*a0)))
        R.append(n)
        r_vals.append(c)
    plt.plot(r_vals, R, label=orb)

plt.title("Radial Factor Plot")
plt.xlabel("Distance from nucleus (r/a0)")
plt.ylabel("Radial wave function R(r)")
plt.legend(loc="upper right")
plt.axhline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
