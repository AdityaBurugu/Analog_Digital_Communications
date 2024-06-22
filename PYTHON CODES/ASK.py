import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 10  # Carrier frequency
fm = 2   # Message frequency
A = 1    # Amplitude of carrier signal
m_depth = 0.5  # Modulation depth
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time array

# Generate message signal (Pulse Wave)
message_signal = np.where(np.sin(2 * np.pi * fm * t) > 0, 1, 0)

# Generate carrier signal
carrier_signal = A * np.sin(2 * np.pi * fc * t)

# Generate ASK signal
ask_signal = (m_depth * message_signal) * carrier_signal

# Demodulation
demodulated_signal = np.where(ask_signal == 0, 0, 1)

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, message_signal)
plt.title('Message Signal (Pulse Wave)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 2)
plt.plot(t, carrier_signal)
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 3)
plt.plot(t, ask_signal)
plt.title('ASK Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 4)
plt.plot(t, demodulated_signal)
plt.title('Demodulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.suptitle("ASK Modulation")
plt.tight_layout()
plt.show()
