import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 5

print("Recording...")

recording = sd.rec(int(seconds * fs),
                   samplerate=fs,
                   channels=2)

sd.wait()

write("output.wav", fs, recording)

print("Recording Saved!")