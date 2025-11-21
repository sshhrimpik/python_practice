import turtle

turtle.shape('turtle')

side = 50
length = 10
angle = 360 / side

num = 0
while num < 3:
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
    turtle.right(60)
    num += 1

turtle.done()