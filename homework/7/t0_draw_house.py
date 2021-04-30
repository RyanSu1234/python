'''
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle
def house1_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('green')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house1_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('black')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()


def house2_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('orange')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house2_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('saddlebrown')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()

def house3_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('green')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house3_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('saddlebrown')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()

def house4_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house4_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()


def house5_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house5_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('saddlebrown')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()


def house6_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('blue')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house6_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()


def house7_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('green')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house7_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('blue')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()


def house8_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('blue')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house8_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('saddlebrown')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()



def house9_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('red')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house9_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('saddlebrown')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()



def house10_top(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('green')
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
def house10_down(x, y):
    turtle.penup()
    turtle.goto(x+8.5, y)
    turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()











house1_top(0,0)
house1_down(0,0)
house2_top(50,0)
house2_down(50,0)
house3_top(100,0)
house3_down(100,0)
house4_top(150,0)
house4_down(150,0)
house5_top(200,0)
house5_down(200,0)
house6_top(250,0)
house6_down(250,0)
house7_top(0,100)
house7_down(0,100)
house8_top(50,100)
house8_down(50,100)
house9_top(100,100)
house9_down(100,100)
house10_top(150,100)
house10_down(150,100)



























