from ball_OO import *

num_balls = int(input("Number of balls to simulate: "))
balls = []
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

for i in range(num_balls):
    balls.append(Ball(i, canvas_width, canvas_height, ball_radius))

while (True):
    turtle.clear()
    for i in range(num_balls):
        balls[i].draw_circle(ball_radius)
        balls[i].move_circle(canvas_width, canvas_height, ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
