#!python3.10
# coding=utf-8
"""
 Author: courageux_san WX
 Date: 2024-08-20 00:11:39
 LastEditors: courageux_san WX
 LastEditTime: 2024-08-20 00:11:41
 FilePath: /talk-tracker/asr/asr_funasr.py
"""

"""
 chunk_size 是用于流式传输延迟的配置。[0,10,5] 表示实时显示的粒度为 1060=300 毫秒。每个推理输入为 600 毫秒（采样点为 16000*0.6=960），输出为相应的文本。对于最后一个语音片段的输入，需要将 is_final=True 设置为强制输出最后一个词语。

"""


from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
 
model_dir = "iic/SenseVoiceSmall"
 
model = AutoModel(
    model=model_dir,
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 30000},
    device="cuda:0",
)
 
# en
res = model.generate(
    input=f"{model.model_path}/example/en.mp3",
    cache={},
    language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech"
    use_itn=True,
    batch_size_s=60,
    merge_vad=True,  #
    merge_length_s=15,
)
text = rich_transcription_postprocess(res[0]["text"])
print(text)


from funasr import AutoModel

chunk_size = [0, 10, 5]  # [0, 10, 5] 600ms, [0, 8, 4] 480ms
encoder_chunk_look_back = 4  # number of chunks to lookback for encoder self-attention
decoder_chunk_look_back = (
    1  # number of encoder chunks to lookback for decoder cross-attention
)

model = AutoModel(model="iic/paraformer-zh-streaming")

import soundfile
import os

wav_file = os.path.join(model.model_path, "example/asr_example.wav")
speech, sample_rate = soundfile.read(wav_file)
chunk_stride = chunk_size[1] * 960  # 600ms

cache = {}
total_chunk_num = int(len((speech) - 1) / chunk_stride + 1)
for i in range(total_chunk_num):
    speech_chunk = speech[i * chunk_stride : (i + 1) * chunk_stride]
    is_final = i == total_chunk_num - 1
    res = model.generate(
        input=speech_chunk,
        cache=cache,
        is_final=is_final,
        chunk_size=chunk_size,
        encoder_chunk_look_back=encoder_chunk_look_back,
        decoder_chunk_look_back=decoder_chunk_look_back,
    )
    print(res)
