import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, firwin, filtfilt

# Define parameters
fs = 1000  # Sampling frequency
T = 1 / fs  # Sampling period
t = np.arange(0, np.pi, T)  # Time vector

# Message and carrier parameters
a = 1  # Amplitude of the message signal
fm = 1  # Frequency of the message signal
fc = 10  # Frequency of the carrier signal

# Generate carrier and message signals
c = 0.5 * (square(2 * np.pi * fc * t) + 1)
m = a * np.sin(2 * np.pi * fm * t)

# PAM Bipolar Modulated Signal
y = m * c

# Convert to Unipolar PAM
u = np.where(c > 0, y + 2, y)

# Demodulation
dmod = y * c
filter_order = 201
filter_coeffs = firwin(filter_order, fm / (fs / 2), pass_zero='lowpass')
og = filtfilt(filter_coeffs, [1], dmod)

# Plotting
fig, axs = plt.subplots(5, 1, figsize=(10, 12))
fig.suptitle("Pulse Amplitude Modulation and Demodulation")

titles = ['Sinusoidal Signal', 'Carrier Signal', 'PAM Bipolar Waveform', 'PAM Unipolar Waveform', 'PAM Demodulated Waveform']
signals = [m, c, y, u, og]
y_labels = ['Amplitude'] * 5

for ax, signal, title, ylabel in zip(axs, signals, titles, y_labels):
    ax.plot(t, signal)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)  # Add grid for better readability

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
