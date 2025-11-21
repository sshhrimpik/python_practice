import turtle

turtle.shape('turtle')

n = 12
length = 100
angle = 360 / n

count = 0
while count < n:
    turtle.right(360 + angle)
    turtle.forward(length)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(length)
    count = count + 1

turtle.done()