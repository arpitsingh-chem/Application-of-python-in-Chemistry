#Maxwell distribution law
import math
import numpy as np
from numpy import pi
from numpy import arange
import matplotlib.pyplot as plt
r=8.314
m=0.032
T=np.arange(150,10000,1000)
for t in T:
  velocity=[]
  numbers=[]
  for c in arange (1,10000,0.1):
    n=((4*pi)*(m/(2*pi*r*t))**(3/2))*(c**2)*(np.exp(-(m*(c**2)/(2*r*t))))
    velocity.append(c)
    numbers.append(n)
  plt.plot(velocity,numbers,label=(f'T={t}K'))
plt.title("Maxwell distribution law")
plt.xlabel("velocity(m/s)")
plt.ylabel("numbers")
plt.legend(loc="upper right")
plt.show()
