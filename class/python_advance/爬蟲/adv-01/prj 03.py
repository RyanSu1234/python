from tkinter import *


def show_fun():
    print("hello")
    display.config(text="Hello",fg="red",bg="black")

def clear_fun():
    print("hello")
    display.config(text="",fg="white",bg="white")

windows = Tk()
windows.title("My first GUI")

btn1 = Button(windows, text="show screen", command=show_fun)
btn1.pack()
btn2 = Button(windows, text="clear screen", command=clear_fun)
btn2.pack()
display = Label(windows,text="")
display.pack()
display = Label(windows,text="")
display.pack()

windows.mainloop()