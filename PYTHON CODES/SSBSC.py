import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Define parameters
fm = 10  # Message frequency
fc = 100  # Carrier frequency
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector

# Generate message signals
m = np.cos(2 * np.pi * fm * t)  # Message signal with 0 phase shift
mc = np.sin(2 * np.pi * fm * t)  # Message signal with 90-degree phase shift

# Generate carrier signals
c = np.cos(2 * np.pi * fc * t)  # Carrier signal with 0 phase shift
cc = np.sin(2 * np.pi * fc * t)  # Carrier signal with 90-degree phase shift

# Generate SSBSC signals
fx = m * c  # DSBSC signal component
fy = mc * cc  # DSBSC signal component

s1 = fx - fy  # Lower Sideband (LSB) Signal
s2 = fx + fy  # Upper Sideband (USB) Signal

# Plotting
plt.figure(figsize=(10, 12))
plt.suptitle("SSBSC Modulation and Demodulation")

plt.subplot(7, 1, 1)
plt.plot(t, m)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Message Signal")
plt.grid(True)

plt.subplot(7, 1, 2)
plt.plot(t, mc)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Message Signal with 90° Phase Shift")
plt.grid(True)

plt.subplot(7, 1, 3)
plt.plot(t, c)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Carrier Signal")
plt.grid(True)

plt.subplot(7, 1, 4)
plt.plot(t, cc)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Carrier Signal with 90° Phase Shift")
plt.grid(True)

plt.subplot(7, 1, 5)
plt.plot(t, s1)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Lower Sideband (LSB) Signal")
plt.grid(True)

plt.subplot(7, 1, 6)
plt.plot(t, s2)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Upper Sideband (USB) Signal")
plt.grid(True)

# Demodulation of LSB signal
d = s1 * np.cos(2 * np.pi * fc * t)
b, a = butter(5, fm / (fs / 2))
demod = filtfilt(b, a, d)

plt.subplot(7, 1, 7)
plt.plot(t, demod)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Demodulated Signal (LSB)")
plt.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
