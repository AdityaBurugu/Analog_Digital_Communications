import numpy as np
import matplotlib.pyplot as plt

# Provide instructions and get user input for data sequence
print("Please enter the data sequence of binary digits (0 or 1):")
i_d = input("Enter Sequence: ")

# Validate user input
try:
    # Convert input string to list of integers
    a = [int(n) for n in i_d]
    # Ensure all elements are either 0 or 1
    if all(x == 0 or x == 1 for x in a):
        d = np.array(a)
    else:
        raise ValueError("Invalid input. Please enter only binary digits (0 or 1).")
except ValueError as e:
    print(e)
    exit()

# Other parameters
T = 1  # Bit duration
Eb = T / 2  # This will result in unit amplitude waveforms
fc = 3 / T  # Carrier frequency
t = np.linspace(0, 5, 1000)  # discrete time sequence between 0 and 5*T (1000 samples)
N = len(t)  # Number of samples
Nsb = N // len(d)  # Number of samples per bit
dd = np.tile(d, (Nsb, 1)).T  # replicate each bit Nsb times
b = 2 * d - 1  # Convert unipolar to bipolar
bb = np.tile(b, (Nsb, 1)).T
dw = dd.flatten()  # Convert dw to a column vector (colum by column) and convert to a row vector
bw = bb.flatten()  # Data sequence samples
w = np.sqrt(2 * Eb / T) * np.cos(2 * np.pi * fc * t)  # carrier waveform
bpsk_w = bw * w  # modulated waveform

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, dw)
plt.title('Data Sequence (Input)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, w)
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, bpsk_w)
plt.title('BPSK Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()


'''import numpy as np
import matplotlib.pyplot as plt

# Generate random binary sequence
num_bits = 10  # Define the number of bits
random_bits = np.random.randint(2, size=num_bits)  # Generate random binary bits

# Other parameters
T = 1  # Bit duration
Eb = T / 2  # This will result in unit amplitude waveforms
fc = 3 / T  # Carrier frequency
t = np.linspace(0, 5, 1000)  # discrete time sequence between 0 and 5*T (1000 samples)
N = len(t)  # Number of samples
Nsb = N // len(random_bits)  # Number of samples per bit
dd = np.tile(random_bits, (Nsb, 1)).T  # replicate each bit Nsb times
b = 2 * random_bits - 1  # Convert unipolar to bipolar
bb = np.tile(b, (Nsb, 1)).T
dw = dd.flatten()  # Convert dw to a column vector (column by column) and convert to a row vector
bw = bb.flatten()  # Data sequence samples
w = np.sqrt(2 * Eb / T) * np.cos(2 * np.pi * fc * t)  # carrier waveform
bpsk_w = bw * w  # modulated waveform

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, dw)
plt.title('Data Sequence (Random Input)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, w)
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, bpsk_w)
plt.title('BPSK Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
'''
