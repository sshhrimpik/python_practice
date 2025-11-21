import turtle

turtle.shape('turtle')
turtle.left(90)

side = 10
length = 10
angle = 360 / side

num = 0
while num < 15:
    count = 0
    while count < side:
        turtle.forward(length)
        turtle.left(angle)
        count += 1
    count = 0
    while count < side:
        turtle.forward(length)
        turtle.right(angle)
        count += 1
    num += 1
    length += 10
    side += 10

turtle.done()