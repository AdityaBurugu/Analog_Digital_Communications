import numpy as np
import matplotlib.pyplot as plt

def generate_random_bits(num_bits):
    """Generate random binary bits."""
    return np.random.randint(2, size=num_bits)

def differential_encode(bits):
    """Differential encoding."""
    encoded_bits = np.zeros_like(bits)
    encoded_bits[0] = bits[0]  # Set the first bit as it is
    for i in range(1, len(bits)):
        encoded_bits[i] = bits[i] ^ bits[i-1]  # XOR operation for differential encoding
    return encoded_bits

def generate_dpsk_signal(encoded_bits, duration=5, num_samples=1000, carrier_freq=3):
    """Generate DPSK modulated signal."""
    T = duration / len(encoded_bits)  # Bit duration
    Eb = T / 2  # Energy per bit
    t = np.linspace(0, duration, num_samples)  # Time vector
    carrier_signal = np.sqrt(2 * Eb / T) * np.cos(2 * np.pi * carrier_freq * t)  # Carrier signal
    modulated_signal = np.zeros_like(t)  # Initialize modulated signal
    phase = 0  # Initial phase
    for i, bit in enumerate(encoded_bits):
        phase += np.pi * bit  # Phase shift based on bit value (0 or 1)
        modulated_signal[i * num_samples // len(encoded_bits): (i + 1) * num_samples // len(encoded_bits)] = \
            np.cos(2 * np.pi * carrier_freq * t[i * num_samples // len(encoded_bits): (i + 1) * num_samples // len(encoded_bits)] + phase)
    return t, carrier_signal, modulated_signal

def plot_signals(t, bits, carrier_signal, modulated_signal):
    """Plot input bits, carrier signal, and modulated signal."""
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    # Plot input bits
    axes[0].stem(np.arange(len(bits)), bits, markerfmt='ro', linefmt='r-', basefmt=' ')
    axes[0].set_title('Input Binary Bits')
    axes[0].set_ylabel('Bit Value')
    axes[0].set_xlabel('Bit Index')

    # Plot carrier signal
    axes[1].plot(t, carrier_signal)
    axes[1].set_title('Carrier Signal')
    axes[1].set_ylabel('Amplitude')

    # Plot modulated signal
    axes[2].plot(t, modulated_signal)
    axes[2].set_title('DPSK Modulated Signal')
    axes[2].set_ylabel('Amplitude')
    axes[2].set_xlabel('Time')

    plt.tight_layout()
    plt.show()

# Generate random bits
num_bits = 5
bits = generate_random_bits(num_bits)

# Differential Encoding
encoded_bits = differential_encode(bits)

# Generate DPSK modulated signal
t, carrier_signal, modulated_signal = generate_dpsk_signal(encoded_bits)

# Plot signals
plot_signals(t, bits, carrier_signal, modulated_signal)
