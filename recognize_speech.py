import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import os
from time import sleep

fs = 44100
dur = 3

sd.default.samplerate = fs
sd.default.channels = 2

r = sr.Recognizer()

for i in range (5, 0, -1):
    print(f"start speaking in {i} second")
    sleep(1)

speak = sd.rec(int(fs * dur))
sd.wait()

sf.write("speech.wav", speak, fs)
sleep(1)

aud = sr.AudioFile("speech.wav")

with aud as src:
    #r.adjust_for_ambient_noise(src)
    audio = r.listen(src)

done = r.recognize_google(audio)

try:
    print(f"I think you said: {done}")
except "UnknownValueError":
    print("Google couldn't understand what you saying bruv")