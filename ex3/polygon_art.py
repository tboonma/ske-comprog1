import turtle
import random


def polygon(x, y, size, n, clr):  # draw polygon
    turtle.penup()
    turtle.color(clr)
    turtle.fillcolor(clr)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(size)
        turtle.left(360 / n)
    turtle.end_fill()
    turtle.penup()


def random_turtle():  # random turtle position and polygon
    size = random.randint(20, 100)
    n = random.randint(3, 8)
    x = random.randint(-350, 350 - size * (n // 2))
    y = random.randint(-350, 350 - size * (n // 2))
    return x, y, n, size


for i in range(20):  # draw twenty polygons
    x, y, n, size = random_turtle()
    polygon(x, y, size, n, "blue")
