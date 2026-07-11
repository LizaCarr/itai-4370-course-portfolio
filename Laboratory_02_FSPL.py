"""Laboratory 02: Free-Space Path Loss at 2.4 GHz."""
import numpy as np
import matplotlib.pyplot as plt

frequency = 2400  # MHz
distances = np.linspace(0.1, 20, 100)  # km
fspl = 20 * np.log10(distances) + 20 * np.log10(frequency) + 32.44

plt.figure(figsize=(8, 5))
plt.plot(distances, fspl, label="FSPL at 2.4 GHz")
plt.xlabel("Distance (km)")
plt.ylabel("Path Loss (dB)")
plt.title("Free-Space Path Loss vs Distance")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
