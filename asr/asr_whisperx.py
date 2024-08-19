#!python3.10
# coding=utf-8
'''
 Author: courageux_san WX
 Date: 2024-08-17 22:47:58
 LastEditors: courageux_san WX
 LastEditTime: 2024-08-19 23:46:33
 FilePath: /talk-tracker/asr/asr_whisperx.py
'''
#!python3.10
# coding=utf-8
"""
 Author: courageux_san WX
 Date: 2024-08-17 22:47:58
 LastEditors: courageux_san WX
 LastEditTime: 2024-08-18 16:46:48
 FilePath: asr/asr_whisperx.py
"""
import time
import whisperx
import numpy as np


device = "cpu"
compute_type = "int8"
start = time.time()
model = whisperx.load_model("base", device, compute_type=compute_type)
end = time.time()
print("加载使用的时间", end - start, "s")


def asr_whisperx(data, language):
    audio = np.frombuffer(data, np.int16).flatten().astype(np.float32) / 32768.0
    result = model.transcribe(
        audio,
        language=language,
        task="transcribe",
        chunk_size=1,
        batch_size=16
        )

    return result["segments"]
