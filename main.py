# coding=utf-8
'''
 Author: courageux_san WX
 Date: 2024-08-18 16:41:29
 LastEditors: courageux_san WX
 LastEditTime: 2024-08-20 01:22:41
 FilePath: /talk-tracker/main.py
'''
import queue
import threading
import pyaudio
from asr.asr_whisperx import asr_whisperx



def record_audio():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while True:
        data = stream.read(CHUNK)
        audio_queue.put(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

def recognize_audio():
    while not stop_flag:
        lock.acquire()
        try:
            data = audio_queue.get()
            result = asr_whisperx(data, language="zh")
            for i in result:
                print(len(data), i)
        except Exception as e:
            print(f"无法识别: {e}")
        finally:
            lock.release()



if __name__ == "__main__":
    lock = threading.Lock()
    stop_flag = False
    audio_queue = queue.Queue()

    audio_thread = threading.Thread(target=record_audio)
    recognize_thread = threading.Thread(target=recognize_audio)
    audio_thread.start()
    recognize_thread.start()
    audio_thread.join()
    recognize_thread.join()
