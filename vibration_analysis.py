import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
# Load accelerometer CSV data 
data = pd.read_csv("Raw Data.csv") 
# Read time and vibration signal 
time = data.iloc[:,0] 
signal = data.iloc[:,4] 
# Calculate sampling interval 
dt = time[1] - time[0] 
# Calculate sampling frequency 
fs = 1 / dt 
# RMS calculation 
rms = np.sqrt(np.mean(signal**2)) 
# FFT analysis 
fft = np.fft.fft(signal) 
# Frequency axis 
freq = np.fft.fftfreq(len(signal), d=dt) 
# Positive frequencies only 
positive_freq = freq[:len(freq)//2] 
positive_fft = np.abs(fft[:len(fft)//2]) 
# Plot FFT spectrum 
plt.plot(positive_freq, positive_fft) 
plt.xlabel("Frequency (Hz)") 
plt.ylabel("Amplitude") 
plt.title("FFT Spectrum of Real Accelerometer Data") 
plt.grid() 
plt.show() 
# Display vibration condition 
if rms > 1: 
 print("High Vibration") 
else: 
 print("Normal Vibration")