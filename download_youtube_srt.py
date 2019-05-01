# -*- coding: utf-8 -*-
import os
from pytube import YouTube

def get_suppport_language(all_captions):
    CN = '''code="zh-CN"'''
    TW = '''code="zh-TW"'''
    EN = '''code="en"'''
    for caption in all_captions:
        if  str(caption).find(CN) != -1:
            return "zh-CN"
    for caption in all_captions:
        if  str(caption).find(TW) != -1:
            return "zh-TW"
    for caption in all_captions:
        if  str(caption).find(EN) != -1:
            return "en"

url = 'https://www.youtube.com/watch?v=aNOZ7ocLD74'

yt = YouTube(url)
###如果报错：“RegexMatchError: regex pattern (\W[\'"]?t[\'"]?: ?[\'"](.+?)[\'"]) had zero matches”
###解决办法：参考如下链接点赞数最高的评论，https://github.com/nficano/pytube/issues/381
# 查看视频支持的字幕
all_captions = yt.captions.all() ## 可看到繁体字的格式code="zh-TW"，简体字为code="zh-CN", 英文为code="en"
code = get_suppport_language(all_captions)
print(code)
##生成字幕
caption = yt.captions.get_by_language_code(code)
##转换字幕为srt格式
srt = caption.generate_srt_captions()
save_path = 'download'
file_with_path = os.path.join(save_path, yt.title + ".txt")
with open(file_with_path, 'w') as f:
  f.write(srt)
