'''
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle


color_list=['red', 'blue', 'green', 'black', 'yellow', 'orange', 'brown','darkblue' ,'maroon', 'olive']


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
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(30)
    turtle.end_fill()







for i in range(10):
    house1_top(-300+i*40, 0, color_list[i])#color_list=['red', 'blue', 'green', 'black', 'yellow', 'orange', 'brown','darkblue' ,'maroon', 'olive']
    house1_down(-300+i*40, 0)































