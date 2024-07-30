import numpy as np
import matplotlib.pyplot as plt

# Define parameters
f1 = 50  # Frequency of the first sine wave
f2 = 120  # Frequency of the second sine wave
Fs = 1000  # Sampling frequency
T = 1  # Duration in seconds

# Time vector
t = np.linspace(0, T, int(Fs * T), endpoint=False)

# Signal
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute FFT
S = np.fft.fft(s)
freqs = np.fft.fftfreq(len(s), 1/Fs)

# Plot the signal
plt.figure(figsize=(14, 6))

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Time Domain Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the FFT (magnitude)
plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(S))
plt.title('Frequency Domain Signal (FFT)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, 200)  # Limit x-axis to relevant range

plt.tight_layout()
plt.show()
