from tkinter import *

def hi_fun():
    print("hello")
def hi_fun():
    print("hello")
    display.config(text="Hi",fg="red",bg="black")
windows = Tk()
windows.title("My first GUI")

btn = Button(windows, text="Click Me", command=hi_fun)
btn.pack()

display = Label(windows,text="")
display.pack()





windows.mainloop()