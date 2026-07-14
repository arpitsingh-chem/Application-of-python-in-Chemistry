import numpy as np
from numpy import arange
import matplotlib.pyplot as plt

# Define a list of temperatures in Kelvin
temp = [605,615,625,635,645,655]

# Loop through each temperature to calculate Van der Waals isotherms
for t in temp:
  volume = []
  pressure = []
  # Loop through a range of volumes
  for v in arange(0.051, 1, 0.0001):
    # Calculate pressure using the Van der Waals equation
    p = ((0.082*t)/(v-0.0305))-5.46/(v**2)
    volume.append(v)
    pressure.append(p)
  # Plot the isotherm for the current temperature
  plt.plot(volume, pressure, label=f'T={t} k')

# Add plot labels and title
plt.title("Van der Waals Isotherm Plot")
plt.xlabel("Volume (L)")
plt.ylabel("Pressure (atm)")
plt.xlim(0.025,0.35) # Set x-axis limits
plt.grid(True, linestyle='--', alpha=0.7) # Add a grid for better readability
plt.legend(loc='upper right') # Display legend
plt.tight_layout() # Adjust layout to prevent labels from being cut off
plt.show() # Show the plot
