# Radial Probability Distribution Curves for Hydrogenic Orbitals
import math
import numpy as np
from numpy import pi
from numpy import arange
import matplotlib.pyplot as plt

a0 = 0.529177 # Bohr radius
Z = 1    # Atomic number (Hydrogen)
orbitals = ['1s', '2s', '2p', '3s']

for orb in orbitals:
    r_vals = []
    p_vals = []
    # Loop through distance r from 0 to 25 with step 0.1
    for r in arange(0, 25, 0.1):
        if orb == '1s':
            R = 2 * (Z/a0)**1.5 * math.exp(-Z*r/a0)
        elif orb == '2s':
            R = (1/(2*math.sqrt(2))) * (Z/a0)**1.5 * (2 - Z*r/a0) * math.exp(-Z*r/(2*a0))
        elif orb == '2p':
            R = (1/(2*math.sqrt(6))) * (Z/a0)**1.5 * (Z*r/a0) * math.exp(-Z*r/(2*a0))
        elif orb == '3s':
            R = (2/(81*math.sqrt(3))) * (Z/a0)**1.5 * (27 - 18*(Z*r/a0) + 2*(Z*r/a0)**2) * math.exp(-Z*r/(3*a0))
        
        # Radial Probability Distribution Function P(r) = r^2 * R^2
        P = (r**2) * (R**2)
        r_vals.append(r)
        p_vals.append(P)
        
    plt.plot(r_vals, p_vals, label=orb)

plt.title("Radial Probability Distribution Curves")
plt.xlabel("Distance from nucleus (r/a0)")
plt.ylabel("Probability Density (4πr²ψ²)")
plt.legend(loc="upper right")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
