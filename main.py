import os
import re

subtitle_lang = "zh"
video_suffix = (".mp4", ".mkv", ".avi", ".wmv", ".mov")
subtitle_suffix = (".srt", ".ass")

file_path = input("Please input video path (default current directory):")
if file_path == '':
    file_path = "./"
else:
    file_path += '/'
vs_match = {}

videos = [i for i in os.listdir(file_path) if i.endswith(video_suffix)]
subtitles = [i for i in os.listdir(file_path) if i.endswith(subtitle_suffix)]
for video in videos:
    SE = re.findall("(S\d+E\d+)", video, re.I)[0]
    vs_match[video] = [x for x in subtitles if SE.upper() in x.upper()]

for k in vs_match:
    print("video:{},subtitle:{}".format(k, vs_match[k]))

check = input("Please confirm to continue(input y or yes):")
if check in ('y', 'yes'):
    for videoInfo in vs_match:
        videoName = os.path.splitext(videoInfo)[0]
        for subtitleName in vs_match[videoInfo]:
            subtitleType = os.path.splitext(subtitleName)[1]
            os.rename(file_path+subtitleName,
                      "{}.zh{}".format(file_path+videoName, subtitleType))
