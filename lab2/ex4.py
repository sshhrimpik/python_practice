import turtle

turtle.shape('turtle')

side = 100
length = 5
angle = 360 / side

count = 0
while count < side:
    turtle.forward(length)
    turtle.left(angle)
    count += 1

turtle.done()
