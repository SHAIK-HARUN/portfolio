import os
import subprocess

audio_dir = r"d:\PORTFOLIO\assets\audio"
os.makedirs(audio_dir, exist_ok=True)
output_wav = os.path.join(audio_dir, "welcome.wav")

text_to_speak = "Hey there. Welcome to my world, A mind full of ideas, a screen full of possibilities, and a passion for making them real."

ps_script = f"""
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile('{output_wav}')
$synth.Rate = -1
$synth.Speak('{text_to_speak}')
$synth.Dispose()
"""

ps_file = os.path.join(audio_dir, "gen.ps1")
with open(ps_file, "w", encoding="utf-8") as f:
    f.write(ps_script)

subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_file], check=True)
print("Successfully generated 10-15s welcome.wav at", output_wav)
