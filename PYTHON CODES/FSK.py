import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Parameters
A = 1.0  # Amplitude
f0 = 2  # Frequency for binary 0
f1 = 10  # Frequency for binary 1
phi = 0  # Phase
bitrate = 1  # Bitrate (bits per second)
duration = 10  # Duration of the signal in seconds

# Generate a random binary message
np.random.seed(0)
message = np.random.randint(2, size=10)  # Generate random binary bits

# Generate the time axis
t = np.linspace(0, duration, int(100 * bitrate * duration))

# Generate continuous carrier signals
carrier_f0 = A * np.cos(2 * np.pi * f0 * t + phi)
carrier_f1 = A * np.cos(2 * np.pi * f1 * t + phi)

# Generate the FSK signal
fsk_signal = np.zeros_like(t)
bit_duration = int(len(t) / len(message))

for i, bit in enumerate(message):
    if bit == 1:
        fsk_signal[i * bit_duration:(i + 1) * bit_duration] = carrier_f1[i * bit_duration:(i + 1) * bit_duration]
    else:
        fsk_signal[i * bit_duration:(i + 1) * bit_duration] = carrier_f0[i * bit_duration:(i + 1) * bit_duration]

# Demodulation using bandpass filters
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

fs = 100 * bitrate  # Sampling frequency
lowcut0 = f0 - 1
highcut0 = f0 + 1
lowcut1 = f1 - 1
highcut1 = f1 + 1

# Apply bandpass filters
filtered_f0 = bandpass_filter(fsk_signal, lowcut0, highcut0, fs, order=6)
filtered_f1 = bandpass_filter(fsk_signal, lowcut1, highcut1, fs, order=6)

# Demodulation
demodulated_message = np.zeros(len(message))
for i in range(len(message)):
    bit_segment_f0 = filtered_f0[i * bit_duration:(i + 1) * bit_duration]
    bit_segment_f1 = filtered_f1[i * bit_duration:(i + 1) * bit_duration]
    if np.sum(bit_segment_f1 ** 2) > np.sum(bit_segment_f0 ** 2):
        demodulated_message[i] = 1
    else:
        demodulated_message[i] = 0

# Plotting
plt.figure(figsize=(12, 18))

# Original binary message
plt.subplot(7, 1, 1)
plt.step(range(len(message)), message, where='mid', label='Message', linestyle='-')
plt.ylabel('Bit Value')
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Continuous carrier signal for f0
plt.subplot(7, 1, 2)
plt.plot(t, carrier_f0, label='Carrier Signal for f0 (Binary 0)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Continuous carrier signal for f1
plt.subplot(7, 1, 3)
plt.plot(t, carrier_f1, label='Carrier Signal for f1 (Binary 1)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Original FSK Signal
plt.subplot(7, 1, 4)
plt.plot(t, fsk_signal, label='FSK Signal')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Filtered signals at f0
plt.subplot(7, 1, 5)
plt.plot(t, filtered_f0, label='Filtered at f0')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Filtered signals at f1
plt.subplot(7, 1, 6)
plt.plot(t, filtered_f1, label='Filtered at f1')
plt.ylabel('Amplitude')
plt.grid()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Comparison of original and demodulated messages
plt.subplot(7, 1, 7)
plt.step(range(len(demodulated_message)), demodulated_message.astype(int), where='mid', label='Demodulated Message')
plt.ylabel('Bit Value')
plt.xlabel('Time [s]')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()

plt.tight_layout()
plt.show()

print("Original Message:    ", message)
print("Demodulated Message: ", demodulated_message.astype(int))