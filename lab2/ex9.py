import turtle
import math

def draw_polygon(n, side_length):
    angle = 360 / n
    sides_drawn = 0
    while sides_drawn < n:
        turtle.forward(side_length)
        turtle.left(angle)
        sides_drawn += 1

turtle.shape('turtle')
turtle.bgcolor("white")

n = 3
count = 0
side_length = 30

while count < 10:
    radius = side_length / (2 * math.sin(math.pi / n))

    turtle.penup()
    turtle.goto(0, -radius)
    turtle.setheading(0)
    turtle.pendown()

    draw_polygon(n, side_length)

    n += 1
    side_length += 15
    count += 1

turtle.hideturtle()
turtle.done()


