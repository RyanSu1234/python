from pytube import YouTube




yt = YouTube("https://www.youtube.com/watch?v=TEqfRq4v-Ds")
print("we are downloading video........................................................................................................ ")

video = yt.streams
length = len(video)

for i in range(length):
    print (video[i])

print("影片名稱:",yt.title)
print("影片作者:",yt.author)
print("影片長度:",yt.length,"秒")
print("影片網址:",yt.thumbnail_url)