import os

print("Duration: ")
duration = input()  # seconds

print("Freq: ")
freq = input() # Hz

os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
