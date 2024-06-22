import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth, firwin, lfilter

# Signal parameters
fs = 1000  # Sampling frequency (Hz)
T = 1 / fs  # Sampling period (seconds)
t = np.arange(0, 2 * np.pi, T)  # Time vector

# Carrier and message signals
fc = 10  # Carrier frequency (Hz)
fm = 1  # Message frequency (Hz)
c = sawtooth(2 * np.pi * fc * t)  # Carrier signal (sawtooth)
m = np.cos(2 * np.pi * fm * t)  # Message signal (cosine)

def generate_pwm(m, c):
    return (m >= c).astype(int)

# PWM generation (vectorized)
pwm = generate_pwm(m,c)  # Efficient comparison and conversion to int


# Plotting the signals
plt.figure(figsize=(10, 6))  # Adjust figure size as needed

plt.subplot(3, 1, 1)
plt.plot(t, m)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, c)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Carrier Signal')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, pwm)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('PWM Signal')
plt.grid(True)

plt.suptitle("PWM - Signal Processing", fontsize=12)
plt.tight_layout()
plt.show()
