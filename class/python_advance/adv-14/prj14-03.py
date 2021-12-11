from moviepy.editor import *      
from pytube import YouTube      
from tkinter import *      
from moviepy.editor import VideoFileClip      
import os     

   

print("we are downloading video...")    

def mp4_change():
    chk_mp3_cut=state.get()
    if (chk_mp3_cut):
        box_entry1 = chk_mp3_cut.get()
        box_entry2 = chk_mp3_cut.get()

    clip =VideoFileClip(video_path)

    if (chk_mp3_cut):
        clip = clip.subclip(box_entry1, box_entry2)
    video_path = "adv-14/prj14-movie/龍貓.mp4"      
    if os.path.isfile(video_path):      
        clip = VideoFileClip(video_path)      
    else:      
        exit()      
    base_path = "adv-14/prj14-movie/"
    if(chk_mp3_cut):
        new_file = "龍貓-cut"
    else:
        new_file = "龍貓"

    new_path = base_path + new_file + ".mp3"      
        
    i=0;      
    while os.path.isfile(new_path):      
        i+=1      
        new_path = base_path + new_file + str(i) + ".mp3"      
             
    clip.audio.write_audiofile(new_path)      
    print("Convert mp3 Success")
    

def show_entry():      
    chk=state.get()      
    
    if(chk):            
        box_entry1.grid(row=1, column=0, sticky="w")
        box_entry2.grid(row=2, column=0, sticky="w")     
        box_entry1_info.grid(row=1, column=1, sticky="w")
        box_entry2_info.grid(row=2, column=1, sticky="w") 

    else:
        box_entry1.grid_forget()
        box_entry1_info.grid_forget()
        box_entry2.grid_forget()
        box_entry2_info.grid_forget()

windows = Tk()      
windows.title("My grid")      
    

box_entry= Label(windows, text="請輸入影片名稱", font=('Arial', 12))
box_entry.grid(row=0, column=0)
box_entry_info = Entry(windows)
box_entry_info.grid(row=0, column=1)

box_entry1 = Label(windows, text="請輸入影片開始時間", font=('Arial', 12))
box_entry1_info = Entry(windows)

box_entry2 = Label(windows, text="請輸入影片結束時間", font=('Arial', 12))
box_entry2_info = Entry(windows)

state=BooleanVar()      
state.set(False)      
box = Checkbutton(windows, text="mp3 cc", var=state, command=show_entry)      
box.grid(row=4, column=0, sticky="w")      
    
btn = Button(windows, text='開始轉換', command=mp4_change)
btn.grid(row=5, columnspan=3)

windows.geometry("300x150")      
windows.mainloop()      






























