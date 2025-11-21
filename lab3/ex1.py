import turtle
import random

turtle.color("red")
turtle.shape('turtle')
turtle.speed(50)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

steps = 500
step_length = 10
count = 0

while count < steps:
    angle = random.uniform(0, 360)
    turtle.left(angle)
    turtle.forward(step_length)
    turtle.right(angle)
    count += 1

turtle.done()
