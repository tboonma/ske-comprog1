import random
import turtle


class Ball:
    def __init__(self, ball_id, canvas_width, canvas_height, ball_radius):
        self.__id = ball_id
        self.__xpos = random.randint(-1 * canvas_width + ball_radius, canvas_width - ball_radius)
        self.__ypos = random.randint(-1 * canvas_height + ball_radius, canvas_height - ball_radius)
        self.__vx = random.randint(1, 0.025 * canvas_width)
        self.__vy = random.randint(1, 0.025 * canvas_width)
        self.__ball_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def draw_circle(self, ball_radius):
        turtle.penup()
        turtle.color(self.__ball_color)
        turtle.fillcolor(self.__ball_color)
        turtle.goto(self.__xpos, self.__ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(ball_radius)
        turtle.end_fill()

    def move_circle(self, canvas_width, canvas_height, ball_radius):
        self.__xpos += self.__vx
        self.__ypos += self.__vy
        if abs(self.__xpos + self.__vx) > (canvas_width - ball_radius):
            self.__vx = -(self.__vx)
        if abs(self.__ypos + self.__vy) > (canvas_height - ball_radius):
            self.__vy = -(self.__vy)

    def __str__(self):
        return self.__id, self.__xpos, self.__ypos, self.__vx, self.__vy, self.__ball_color
