from tkinter import *
import datetime


def get_date():
    time = datetime.date.today()
    put_data.configure(text=time, fg='red')


def get_time():
    time = datetime.datetime.now().time()
    put_data.configure(text=time, fg='green')






windows = Tk()
windows.title("My first GUI")

canvas = Canvas(windows, width=50, height=50)
canvas.pack()

put_data = Label(windows, text="")
put_data.pack()

btn = Button(windows, text='獲得現在時間', command=get_time)
btn.pack()

btn1 = Button(windows, text='獲得今天日期', command=get_date)
btn1.pack()





windows.mainloop()