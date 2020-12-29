LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.4",LAB)

from turtlelab6 import turtle,home,mozart,raph,check
from math import sqrt,atan2,degrees
def walkto(x,y):
    """Have Turtle walk straight to location (x,y)"""
    dx = x - turtle.x
    dy = y - turtle.y
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dy,dx))
    turtle.left(angle-turtle.heading) # Turtle's current heading may not be 0
    turtle.forward(dist)

def check_route(x,y,from_x,from_y):
    dx = x - from_x
    dy = y - from_y
    dist = sqrt(dx**2 + dy**2)
    return dist

route1 = check_route(mozart.x,mozart.y,turtle.x,turtle.y) + check_route(raph.x,raph.y,mozart.x,mozart.y) + check_route(home.x,home.y,raph.x,raph.y)
route2 = check_route(raph.x,raph.y,turtle.x,turtle.y) + check_route(mozart.x,mozart.y,raph.x,raph.y) + check_route(home.x,home.y,mozart.x,mozart.y)
if route1 < route2:
    walkto(mozart.x,mozart.y)
    walkto(raph.x,raph.y)
else:
    walkto(raph.x,raph.y)
    walkto(mozart.x,mozart.y)
walkto(home.x,home.y)

check()
