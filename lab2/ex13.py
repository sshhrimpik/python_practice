import turtle

turtle.shape('turtle')

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-35, 35)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(35, 35)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, 0)
turtle.setheading(-60)
turtle.pendown()
turtle.color("red")
turtle.width(5)
turtle.circle(50, 120)

turtle.done()
