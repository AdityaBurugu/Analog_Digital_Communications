import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Clear all previous plots and close all figures
plt.close('all')

# Define time vector
t = np.arange(-5, 5, 0.01)

# Define modulation parameters
fm = 1  # Message frequency
fc = 10  # Carrier frequency

# Generate message and carrier signals
m = np.sin(2 * np.pi * fm * t)  # Message signal
c = np.sin(2 * np.pi * fc * t)  # Carrier signal

# DSBSC Modulated signal
s = m * c

# Demodulation (coherent detection)
d = s * np.sin(2 * np.pi * fc * t)  # Mixing with the carrier

# Low-pass filter to extract the original message signal
b, a = butter(5, fm / (0.5 * (1 / 0.01)))  # Design low-pass filter
dmod = filtfilt(b, a, d)  # Apply low-pass filter

# Plotting
plt.figure(figsize=(10, 8))
plt.suptitle("DSBSC Modulation and Demodulation")

plt.subplot(4, 1, 1)
plt.plot(t, m)
plt.title("Message Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, c)
plt.title("Carrier Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, s)
plt.title("DSBSC Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, dmod)
plt.title("Demodulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
