import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from time import sleep

fs = 44100
dur = 3

sd.default.samplerate = fs
sd.default.channels = 2

r = sr.Recognizer()

def recognize():
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
    try:
        recognized_speech = r.recognize_google(audio)
    except sr.UnknownValueError:
        return "couldn't recognize what was said, try again"

    return recognized_speech