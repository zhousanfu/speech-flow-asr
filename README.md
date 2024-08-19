

<!--
 * @Author: courageux_san WX
 * @Date: 2024-08-17 18:54:47
 * @LastEditors: courageux_san WX
 * @LastEditTime: 2024-08-20 05:48:39
 * @FilePath: /speech-flow-asr/README.md
-->
## 实时语音转录面临的难题
- **流式实时转录**:
    
    语音输入过程中实时转化为文本;
    
- **VAD断句(语音活动检测)**:
    
    语音信号分段转录,提高准确率和流畅度;
    
    VAD的检测算法有多种，比较简单的一种算法是通过短时能量(STE，short time energy)和短时过零率(ZCC，zero cross counter)利用能量的特征来进行检测。短时能量就是指一帧语音信号的能量，过零率则是指一帧语音的时域信号穿过0的次数。除此之外，有些VAD检测算法会综合多个维度的语音特征包括能量特征、频域特征、倒谱特征、谐波特征、长时信息特征



## ASR模型文章:
SenseVoice 

https://github.com/k2-fsa/sherpa-onnx 基于Kaldi

https://www.bilibili.com/video/BV1Nm421G7kN/?spm_id_from=333.788&vd_source=e8123f432ea799e442342a21d50afb9a

13个最佳开源语音识别引擎[文章地址](https://mp.weixin.qq.com/s/YhI6Bk7ssnmnNBISV4nPjw)

常用语音识别开源四大工具：Kaldi，PaddleSpeech，WeNet，EspNet[文章地址](https://robinfang.blog.csdn.net/article/details/138426596?spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ECtr-6-138426596-blog-136822850.235%5Ev43%5Epc_blog_bottom_relevance_base4&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ECtr-6-138426596-blog-136822850.235%5Ev43%5Epc_blog_bottom_relevance_base4&utm_relevant_index=11)