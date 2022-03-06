from pytube import YouTube
from moviepy.editor import VideoFileClip

yt = YouTube("https://www.youtube.com/watch?v=TEqfRq4v-Ds")
print("we are downloading video... ")

video = yt.streams
result = video.filter(progressive=True, subtype="mp4", res="360p")
print(result[0])

dest = "adv-12/"
fname = "普拿疼迷因"

result[0].download(output_path=dest,filename=fname)
print("download finish...")

clip=VideoFileClip(dest+fname)
clip.preview()
