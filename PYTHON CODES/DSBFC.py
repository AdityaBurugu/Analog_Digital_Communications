import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Define parameters
fs = 1000  # Sampling frequency
T = 1 / fs  # Sampling period
t = np.arange(0, 2, T)  # Time vector
fm = 5  # Message signal frequency
fc = 100  # Carrier signal frequency

# Generate signals
am = 0.5
ac = 1
m = am * np.cos(2 * np.pi * fm * t)
c = ac * np.cos(2 * np.pi * fc * t)
s_under = (ac + 0.5 * m) * np.cos(2 * np.pi * fc * t)
s_critical = (ac + m) * np.cos(2 * np.pi * fc * t)
s_over = (ac + 1.5 * m) * np.cos(2 * np.pi * fc * t)

# Demodulation
d_critical = s_critical * c  # Demodulate by multiplying with carrier
b, a = butter(4, fm / (fs / 2))  # Design the low-pass filter
dmod_critical = filtfilt(b, a, d_critical)

# Plotting
plt.figure(figsize=(10, 12))
plt.suptitle("DSBFC Modulation and Demodulation")

signals = [m, c, s_under, s_critical, s_over, dmod_critical]
titles = ["Message Signal", "Carrier Signal", "Under Modulation", "Critical Modulation", "Over Modulation", "Demodulated Signal"]
y_labels = ["Amplitude"] * 6

for i, (signal, title, ylabel) in enumerate(zip(signals, titles, y_labels), 1):
    plt.subplot(6, 1, i)
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel(ylabel)
    plt.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
