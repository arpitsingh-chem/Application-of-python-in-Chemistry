# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange

# Define physical constants
h = 6.626 * 10**(-34)  # Planck's constant
c = 2.997925 * 10**8   # Speed of light
k = 1.381 * 10**(-23)  # Boltzmann constant

# Define a range of temperatures to simulate
temp = [2000, 4000, 5000, 6000]

# Loop through each temperature
for t in temp:
  # Initialize lists to store wavelength and intensity values for the current temperature
  wavelength = []
  intensity = []

  # Loop through a range of wavelengths from 1 nm to 3 µm with 1 nm steps
  for w in arange(1e-9, 3e-6, 1e-9):
    # Calculate the 'a' component of Planck's law
    a = 2.0 * h * c**2
    # Calculate the 'b' component of Planck's law (exponent term)
    b = h * c / (w * k * t)

    # Add a condition to handle cases where 'b' is too large to prevent overflow
    if b > 700:
      i = 0.0
    else:
      # Calculate the intensity 'i' using Planck's law formula
      i = a / ((w**5) * (np.exp(b) - 1))

    # Append the calculated wavelength and intensity to their respective lists
    wavelength.append(w)
    intensity.append(i)

  # Plot the intensity vs. wavelength for the current temperature
  plt.plot(wavelength, intensity, label=f'T={t} k')

# Add title and labels to the plot
plt.title("Planck’s distribution law")
plt.xlabel("Wavelength (m)")
plt.ylabel("Intensity (W/m^3)")

# Display the legend
plt.legend(loc='upper right')

# Add user's name(Optional)
plt.figtext(0.99, 0.01, 'Arpit Singh', horizontalalignment='right', fontsize=10, color='gray')

# Show the plot
plt.show()