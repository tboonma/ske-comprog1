import turtle
import random

clr_list = ['red', 'blue', 'gold', 'brown', 'violet', 'pink', 'orange', 'yellow']
turtle.hideturtle()


def pinwheel(num_branch, size, backup):
    x = random.randint(-100, 100)  # random more variable
    y = random.randint(-50, 150)
    pensize = random.randint(1, 8)
    global clr_list
    temp = random.randint(0, 7)
    color = clr_list[temp]
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.pendown()  # turtle start drawing
    for i in range(num_branch):
        turtle.forward(size)
        turtle.forward(-backup)
        turtle.right(360 / num_branch)
    turtle.penup()


for i in range(10):
    temp = random.randint(0, 7)
    color = clr_list[temp]
    num_branch = random.randint(5, 15)
    size = random.randint(80, 150)
    backup = random.randint(0, size)
    pinwheel(num_branch, size, backup)

turtle.done()  # hold the turtle after finish
