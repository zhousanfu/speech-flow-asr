#!python3.10
# coding=utf-8
'''
 Author: courageux_san WX
 Date: 2024-08-17 18:54:06
 LastEditors: courageux_san WX
 LastEditTime: 2024-08-19 07:22:05
 FilePath: /talk-tracker/asr/asr_vosk.py
'''
import vosk
import pyaudio



# Set up audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 8192

model = vosk.Model("models/vosk-model-small-cn-0.22")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Create a PyAudio object
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
while True:
    data = stream.read(CHUNK)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)
stream.stop_stream()
stream.close()
p.terminate()

