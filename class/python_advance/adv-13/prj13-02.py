from moviepy.editor import *
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

yt = YouTube("https://youtu.be/-tAOBkFcPrM")
print("we are downloading video...")

video = yt.streams
result = video.filter(progressive=True, subtype="mp4", res="360p")
print(result[0])

dest = "adv-13/"
fname = "小小兵.mp4"

result[0].download(output_path=dest,filename=fname)
print("download finish...")

video_path = "adv-13/小小兵.mp4"
if os.path.isfile(video_path):
    clip = VideoFileClip(video_path)
    clip = clip.subclip(8, 20)
else:
    exit()

base_path = "adv-13/"
new_file = "小小兵-Cut"
new_path = base_path + new_file + ".gif"

i=0;
while os.path.isfile(new_path):
    i+=1
    new_path = base_path + new_file + str(i) + ".gif"

print(new_path)
clip.write_gif(new_path)