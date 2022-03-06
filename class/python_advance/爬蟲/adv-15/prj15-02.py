from tkinter import *
from moviepy.editor import *
import os     

def get_cut():
    
    print(rad_val)

def mp4_change():
    chk_mp3_cut=state.get()
    if (chk_mp3_cut):
        box_entry1 = box_entry1_info.get()
        box_entry2 = box_entry2_info.get()
        
    video_path = "adv-14/prj14-movie/龍貓.mp4"      
    clip =VideoFileClip(video_path)

    if (chk_mp3_cut):
        clip = clip.subclip(box_entry1, box_entry2)
    if os.path.isfile(video_path):      
        clip = VideoFileClip(video_path)      
    else:      
        exit()      
    base_path = "adv-14/prj14-movie/"
    if(chk_mp3_cut):
        new_file = "龍貓-cut"
    else:
        new_file = "龍貓"

    sub_name = ""
    rad_val = sel.get()
    if (rad_val ==0):
        sub_name = ".mp4"
    elif(rad_val ==1):
        sub_name = ".gif"
    else:
        sub_name = ".mp3"


    new_path = base_path + new_file + sub_name      

    i=0;      
    while os.path.isfile(new_path):      
        i+=1      
        new_path = base_path + new_file + str(i) + sub_name      
    if (rad_val ==0):
        clip.write_videofile(new_path)      
        print("Convert mp4 Success")
    elif(rad_val ==1):
        clip.write_gif(new_path) 
    else:
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
windows.title("My Viedo")    


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

sel = IntVar()
sel.set(1)
rad1 = Radiobutton(windows, text="mp4", value=0, var=sel)
rad1.grid(row=3, column=0)
rad2 = Radiobutton(windows, text="gif", value=1, var=sel)
rad2.grid(row=3, column=1)
rad3 = Radiobutton(windows, text="mp3", value=2, var=sel)
rad3.grid(row=3, column=2)

windows.geometry("350x350")
windows.mainloop()
