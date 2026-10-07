import os
import wave
import audioop

wav_path = r"d:\PORTFOLIO\assets\audio\welcome.wav"

with wave.open(wav_path, "rb") as wf:
    n_channels = wf.getnchannels()
    sampwidth = wf.getsampwidth()
    framerate = wf.getframerate()
    n_frames = wf.getnframes()
    data = wf.readframes(n_frames)

max_val = audioop.max(data, sampwidth)
print(f"Current Max Peak Amplitude: {max_val}")

if max_val > 0:
    factor = 30000.0 / max_val
    print(f"Amplifying volume by factor of {factor:.2f}x")
    amplified_data = audioop.mul(data, sampwidth, factor)
else:
    amplified_data = data

with wave.open(wav_path, "wb") as wf:
    wf.setnchannels(n_channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(amplified_data)

print("Successfully amplified welcome.wav to peak volume clarity!")
