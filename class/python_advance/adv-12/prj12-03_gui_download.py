from pytube import YouTube
from moviepy.editor import VideoFileClip
from tkinter import*
import requests, json


def get_movie():
    get_url = url_info.get();
    get_name = name_info.get() + ".mp4";
    yt = YouTube(get_url)
    print("we are downloading video... ")

    video = yt.streams
    result = video.filter(progressive=True, subtype="mp4", res="360p")
    print(result)

    dest = "adv-12/"
    fname = get_name

    result[0].download(output_path=dest,filename=fname)
    print("download finish...")

    movie_name.config(text="movie name = " + get_name)
    movie_time.config(text="movie time = " + str(yt.length) + " sec")


windows = Tk()
windows.title("movie")

url = Label(windows, text="請輸入下載網址", font=('Arial', 12))
url.grid(row=0, column=0)
url_info = Entry(windows)
url_info.grid(row=0, column=1)

name = Label(windows, text="請輸入影片名稱", font=('Arial', 12))
name.grid(row=1, column=0)
name_info = Entry(windows)
name_info.grid(row=1, column=1)

btn = Button(windows, text='Download', command=get_movie)
btn.grid(row=2, columnspan=2)

movie_name = Label(windows, text="")
movie_name.grid(row=3, column=0)
movie_time = Label(windows, text="")
movie_time.grid(row=4, column=0)
movie_res = Label(windows, text="")
movie_res.grid(row=5, column=0)

windows.mainloop()




