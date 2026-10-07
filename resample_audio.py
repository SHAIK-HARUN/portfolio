import os
import wave
import audioop

wav_in = r"d:\PORTFOLIO\assets\audio\welcome.wav"
wav_out = r"d:\PORTFOLIO\assets\audio\welcome.wav"

with wave.open(wav_in, "rb") as in_wf:
    n_channels = in_wf.getnchannels()
    sampwidth = in_wf.getsampwidth()
    framerate = in_wf.getframerate()
    n_frames = in_wf.getnframes()
    data = in_wf.readframes(n_frames)

    resampled_data, _ = audioop.ratecv(data, sampwidth, n_channels, framerate, 44100, None)

with wave.open(wav_out, "wb") as out_wf:
    out_wf.setnchannels(n_channels)
    out_wf.setsampwidth(sampwidth)
    out_wf.setframerate(44100)
    out_wf.writeframes(resampled_data)

print("Resampled welcome.wav to 44100 Hz 16-bit PCM successfully!")
