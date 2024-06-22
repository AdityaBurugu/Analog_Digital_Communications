import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

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


# Perform Pulse Position Modulation (PPM) generation
x1 = ~pwm  # Inverter output
y1 = np.diff(x1.astype(int))  # Differentiator output
ppm = np.zeros(len(y1))
ppm[np.where(y1 == 1)[0]] = 1

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, m)
plt.title('Message Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 2)
plt.plot(t, c)
plt.title('Sawtooth Waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 3)
plt.plot(t, pwm)
plt.title('Pulse Width Modulation (PWM)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 4)
plt.plot(t[:-1], ppm)
plt.title('Pulse Position Modulation (PPM)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
