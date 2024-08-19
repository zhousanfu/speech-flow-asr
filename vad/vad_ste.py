# coding=utf-8
'''
 Author: courageux_san WX
 Date: 2024-08-20 00:26:07
 LastEditors: courageux_san WX
 LastEditTime: 2024-08-20 01:27:11
 FilePath: /talk-tracker/vad/vad_ste.py
'''
"""
auditok提供了一个split函数，可以通过声音信号能量的强弱来判断是否有人说话，从而根据语音的空隙来分割音频，这对于一段长语音的音频做分割时非常重要的，通常ASR模型是无法一次处理过长的音频
"""
import os,auditok



audio = auditok.load("data/test.wav")
audio.plot()

save_slice_path = "data/slice_wav/slice"
#检测音频中的声音进行切分
audio_slices = audio.split(
    min_dur=1,              #包含声音最短的音频长度
    max_dur=15,             #包含声音最长的音频长度,超过这个长度会被切断
    max_silence=0.3,        #音频中没有声音音频的最长长度
    energy_threshold=55     #判断音频中包含声音必须大于这个阈值
)
#切分音频
for i, r in enumerate(audio_slices):
    post_id = os.path.basename(wav_path)[:-4]
    # 输出分割音频中包含的信息
    print("slice wav {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r))
    # 播放分段的音频
    r.play(progress_bar=True)
    # 将分段后的音频保存为wav文件
    audio_name = "{}_{}.wav".format(post_id,i+1)
    save_wav_path = os.path.join(save_slice_path,audio_name)
    filename = r.save(save_wav_path)
    print("save：{}".format(filename))

