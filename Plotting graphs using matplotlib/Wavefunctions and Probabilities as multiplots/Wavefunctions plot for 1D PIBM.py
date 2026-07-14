# Import necessary libraries for plotting and numerical operations.
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from numpy import pi

# Define quantum numbers 'n' to be plotted.
number = np.arange(0,5,1)

# Loop through each quantum number.
for n in number:
  radius = []
  wavefunction =[]
  # Calculate wavefunction 'y' for positions 'r' from 0 to 1.
  for r in np.arange(0,1,0.002):
    # Formula for a particle in a 1D box (L=1).
    y =(np.sqrt(2/1)*np.sin(n*np.pi*r))
    radius.append(r)
    wavefunction.append(y)
  # Plot the wavefunction for current 'n' with a label for the legend.
  plt.plot(radius,wavefunction, label=f'n={n}')

# Set plot title and axis labels.
plt.title("wavefunction curve ")
plt.xlabel("x/L")
plt.ylabel("wavefunction")
# Display the legend to identify each curve.
plt.legend(loc='upper right')
# Show the plot.
plt.show()
