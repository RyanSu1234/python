from tkinter import *

def move_circle(event):
    key=event.keysym
    print('key')
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)    




windows = Tk()
windows.title("My first GUI")
canvas = Canvas(windows, width=600, height=600)
canvas.pack()
circle = canvas.create_oval(100, 100, 300, 300, fill="red")
canvas.bind_all('<key>', move_circle)



rect = canvas.create_rectangle(220,400,340,430,fill="blue")

msg = canvas.create_text(300, 100, text="corcodile",fill="black",font = ('Arial', 30))

img = PhotoImage(file="adv-02/crocodile2.gif")
my_img = canvas.create_image(300, 300, image = img)

windows.mainloop()