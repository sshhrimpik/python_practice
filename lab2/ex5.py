import turtle

turtle.shape('turtle')

side_length = 20
step = 20
squares = 10

count = 0
while count < squares:
    turtle.penup()
    turtle.goto(-side_length / 2, -side_length / 2)
    turtle.pendown()

    side = 0
    while side < 4:
        turtle.forward(side_length)
        turtle.left(90)
        side += 1

    side_length += step
    count += 1

turtle.done()

