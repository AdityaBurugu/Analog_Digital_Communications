import numpy as np
import matplotlib.pyplot as plt

# PCM signal generation parameters
f = 2
a = 3
fs = 20 * f
duration = 2
t = np.arange(0, duration, 1/fs)

# Generate analog signal
x = a * np.sin(2 * np.pi * f * t)

# Quantization and level shifting
q_op = np.round(x + a)

# Encoder
enco = np.unpackbits(q_op.astype(np.uint8))
# Decoding and shifting amplitude level
deco = np.packbits(enco).astype(np.int16) - a

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(5, 1, 1)
plt.plot(t, x)
plt.title('Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 2)
plt.stem(t, x)
plt.title('Analog Signal (Stem Plot)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 3)
plt.plot(t, q_op)
plt.title('Quantized Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 4)
plt.stairs(enco)
plt.title('Encoded Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(5, 1, 5)
plt.plot(t, deco, 'r')
plt.title('Decoded Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()