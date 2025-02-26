import numpy as np
import pyaudio

# Parameters for the sine wave
frequency = 440  # Frequency in Hertz (e.g., A4 note)
duration = 2  # Duration in seconds

# Generate the sine wave
t = np.linspace(0, duration, int(44100 * duration), endpoint=False)
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Play the sine wave
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
stream.write(sine_wave.tobytes())
stream.stop_stream()
stream.close()
audio.terminate()