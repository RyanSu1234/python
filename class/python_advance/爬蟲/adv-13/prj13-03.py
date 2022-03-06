from moviepy.editor import *
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
from tkinter import*
import requests, json

def movie_cut():
    video_path = "adv-13/prj13-movie/" + url_info.get()

    print(video_path)

    start_time = name_info.get()
    end_time = name1_info.get()

    if os.path.isfile(video_path):
        clip = VideoFileClip(video_path)
        clip = clip.subclip(start_time,end_time)
    else:
        exit()

    base_path = "adv-13/prj13-movie/"
    new_file = "小小兵-Cut"
    new_path = base_path + new_file + ".mp4"

    i=0;
    while os.path.isfile(new_path):
        i+=1
        new_path = base_path + new_file + str(i) + ".mp4"

    clip.write_videofile(new_path)
    movie_name.config(text="切割完畢")



windows = Tk()
windows.title("movie")

url = Label(windows, text="請輸入影片名稱", font=('Arial', 12))
url.grid(row=0, column=0)
url_info = Entry(windows)
url_info.grid(row=0, column=1)

name = Label(windows, text="請輸入影片開始時間", font=('Arial', 12))
name.grid(row=1, column=0)
name_info = Entry(windows)
name_info.grid(row=1, column=1)

name1 = Label(windows, text="請輸入影片結束時間", font=('Arial', 12))
name1.grid(row=2, column=0)
name1_info = Entry(windows)
name1_info.grid(row=2, column=1)

btn = Button(windows, text='切割影片', command=movie_cut)
btn.grid(row=3, columnspan=2)

movie_name = Label(windows, text="")
movie_name.grid(row=3, column=0)

windows.mainloop()