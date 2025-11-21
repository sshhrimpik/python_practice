import turtle

turtle.shape('turtle')

length = 10
increment = 5
steps = 40

count = 0
while count < steps:
    turtle.forward(length)
    turtle.right(90)
    length += increment
    count += 1

turtle.done()
