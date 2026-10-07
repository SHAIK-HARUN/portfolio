
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile('d:\PORTFOLIO\assets\audio\welcome.wav')
$synth.Rate = -1
$synth.Speak('Hey there. Welcome to my world, A mind full of ideas, a screen full of possibilities, and a passion for making them real.')
$synth.Dispose()
