import turtle

turtle.shape('turtle')

def draw_star(n, size):
    if n < 5 or n % 2 == 0:
        print("star must have an odd number of vertices >= 5")
        return
    angle = 180 - (180 / n)
    steps = 0
    while steps < n:
        turtle.forward(size)
        turtle.right(angle)
        steps += 1

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
draw_star(5, 100)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
draw_star(11, 80)

turtle.done()
