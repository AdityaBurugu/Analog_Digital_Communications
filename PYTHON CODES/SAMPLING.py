import numpy as np
import matplotlib.pyplot as plt

# Continuous Time Signal
t = np.arange(-10, 10, 0.01)
T = 4
fm = 1 / T
x = np.sin(np.pi * fm * t) + np.cos(2 * np.pi * fm * t)
plt.subplot(3, 2, 1)
plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Continuous Time Signal")

# Sampling at 1.2fm
fs1 = 1.2 * fm
n1 = np.arange(-4, 5, 1)
x1 = np.sin(np.pi * fm * n1 / fs1) + np.cos(2 * np.pi * fm * n1 / fs1)
plt.subplot(3, 2, 2)
plt.stem(n1, x1)
plt.plot(n1, x1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Overlap")

# Sampling at 2fm (Nyquist Rate)
fs2 = 2 * fm
n2 = np.arange(-5, 6, 1)
x2 = np.sin(np.pi * fm * n2 / fs2) + np.cos(2 * np.pi * fm * n2 / fs2)
plt.subplot(3, 2, 3)
plt.stem(n2, x2)
plt.plot(n2, x2)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Nyquist")

# Sampling at 8fm (Above Nyquist Rate)
fs3 = 8 * fm
n3 = np.arange(-20, 21, 1)
x3 = np.sin(np.pi * fm * n3 / fs3) + np.cos(2 * np.pi * fm * n3 / fs3)
plt.subplot(3, 2, 4)
plt.stem(n3, x3)
plt.plot(n3, x3)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sampling")

# Reconstruction of Continuous Time Signal
plt.subplot(3, 2, (5,6))
plt.plot(n3, x3)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Reconstruction")

plt.suptitle("SAMPLING THEOREM")
plt.tight_layout()
plt.show()

