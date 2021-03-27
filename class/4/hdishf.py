import turtle

turtle.color('blue')
turtle.shape('turtle')
turtle.penut('')
for step in range(5, 61, 2):
    turtle.stamp()
    turtle.forward(step)
    turtle.right(25)
    print(step)