import turtle

turtle.shape('turtle')
turtle.speed(0)

length = 5

for i in range(80):
    turtle.forward(length)
    turtle.left(20)
    length += 0.5

turtle.done()

