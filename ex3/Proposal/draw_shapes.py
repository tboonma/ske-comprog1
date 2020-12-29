import turtle

# Set to slowest speed and east heading.
# To increase the speed, use the following guide:
# “fast”: 10 “normal”: 6 “slow”: 3 “slowest”: 1

turtle.speed(10)
turtle.setheading(0)

# draw square
turtle.penup()
turtle.color("red")
turtle.fillcolor("green")
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
for i in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

# draw triangle
turtle.penup()
turtle.color("blue")
turtle.fillcolor("yellow")
turtle.goto(0, -100)
turtle.pendown()
turtle.begin_fill()
for i in range (3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()

# draw pentagon
turtle.penup()
turtle.color("red")
turtle.fillcolor("green")
turtle.goto(150, 0)
turtle.pendown()
turtle.begin_fill()
for i in range (5):
    turtle.forward(100)
    turtle.left(72)
turtle.end_fill()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
