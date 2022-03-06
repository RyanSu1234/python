from moviepy.editor import *
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

yt = YouTube("https://www.youtube.com/watch?v=ugk2e_5WZ8E")
print("we are downloading video...")

video = yt.streams
result = video.filter(progressive=True, subtype="mp4", res="360p")
print(result)

dest = "adv-14/prj14-movie/"
fname = "龍貓.mp4"

result[0].download(output_path=dest,filename=fname)
print("download finish...")

video_path = "adv-14/prj14-movie/龍貓.mp4"
if os.path.isfile(video_path):
    clip = VideoFileClip(video_path)
else:
    exit()

base_path = "adv-14/prj14-movie/"
new_file = "龍貓"
new_path = base_path + new_file + ".mp3"

i=0;
while os.path.isfile(new_path):
    i+=1
    new_path = base_path + new_file + str(i) + ".mp3"


clip.audio.write_audiofile(new_path)
print("Convert mp3 Success")

