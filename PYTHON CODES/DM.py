import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000  # Sampling frequency
T = 1 / Fs  # Sampling period
t = np.arange(0, 1, T)  # Time vector

# Input signal (sine wave)
f = 5  # Signal frequency (Hz)
x = np.sin(2 * np.pi * f * t)

# Delta modulation parameters
step_size = 0.5  # Step size for quantization

# Delta modulation
delta_modulated_signal = np.zeros(len(t))
quantized_signal = np.zeros(len(t))

delta = 0  # Initial delta value
for i in range(len(t)):
    quantized_signal[i] = np.sign(x[i] - delta) * step_size
    delta_modulated_signal[i] = delta + quantized_signal[i]
    delta = delta_modulated_signal[i]  # Update delta for next sample

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Input Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, quantized_signal)
plt.title('Quantized Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, delta_modulated_signal)
plt.title('Delta Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
