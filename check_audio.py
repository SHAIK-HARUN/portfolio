import os
import wave
import subprocess

audio_dir = r"d:\PORTFOLIO\assets\audio"
wav_path = os.path.join(audio_dir, "welcome.wav")

if os.path.exists(wav_path):
    with wave.open(wav_path, "rb") as wf:
        print(f"Channels: {wf.getnchannels()}, SampWidth: {wf.getsampwidth()}, FrameRate: {wf.getframerate()}, NumFrames: {wf.getnframes()}")
else:
    print("welcome.wav does not exist!")
