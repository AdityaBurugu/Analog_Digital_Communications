import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Sampling frequency
fs = 1000
# Carrier frequency
fc = 100
# Modulation frequency
fm = 10
# Modulation index
beta = 5
# Time
t = np.arange(0, 1, 1 / fs)

# Modulating signal
x = np.sin(2 * np.pi * fm * t)

# Carrier signal
c = np.cos(2 * np.pi * fc * t)

# Frequency modulation
y = np.cos(2 * np.pi * fc * t + beta * np.sin(2 * np.pi * fm * t))

# Frequency demodulation
analytic_signal = hilbert(y)
instantaneous_phase = np.unwrap(np.angle(analytic_signal))
demodulated = np.diff(instantaneous_phase) * (fs / (2.0 * np.pi * beta))

# Time for demodulated signal (one sample shorter due to differentiation)
t_demod = t[:-1]

# Plot the signals
plt.figure(figsize=(10, 10))
plt.subplot(4, 1, 1)
plt.plot(t, x, label='Modulating signal')
plt.ylabel("Amplitude")
plt.title("Message Signal")
plt.legend()
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, c, label='Carrier signal')
plt.ylabel("Amplitude")
plt.title("Carrier Signal")
plt.legend()
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, y, label='Modulated signal')
plt.ylabel("Amplitude")
plt.title("Modulated Signal (FM)")
plt.legend()
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t_demod, demodulated, label='Demodulated signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Demodulated Signal")
plt.legend()
plt.grid(True)

plt.suptitle("Frequency Modulation and Demodulation")
plt.tight_layout()
plt.show()
