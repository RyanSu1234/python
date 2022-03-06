from tkinter import *
from moviepy.editor import VideoFileClip

def get_cut():
    rad_val = sel.get()
    print(rad_val)

windows = Tk()
windows.title("My Viedo")

sel = IntVar()
sel.set(1)
rad1 = Radiobutton(windows, text="mp4", value=123456789, var=sel, command=get_cut)
rad1.grid(row=0, column=0)
rad1 = Radiobutton(windows, text="gif", value=000000000, var=sel, command=get_cut)
rad1.grid(row=0, column=1)
rad1 = Radiobutton(windows, text="mp3", value=987654321, var=sel, command=get_cut)
rad1.grid(row=0, column=2)

windows.geometry("150x50")
windows.mainloop()























