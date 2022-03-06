from moviepy.editor import *

video_path = "adv-15/小小兵.mp4"

clip = VideoFileClip(video_path)

font_Url="adv-15/TaipeiSansTCBeta-Bold.ttf"

logos=[]

txt_clip = TextClip("水水", font+Font_Url, fontsize=36, color='whit')
txt_clip = txt_clip.set_start(0).set_end(2).set_pos('bottom')
logos.append(txt_clip)

video = CompositeVideoClip([clip, *logos])
video.write_gif("adv-15/小小兵.gif")