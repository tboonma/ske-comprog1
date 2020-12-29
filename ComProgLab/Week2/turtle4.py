from turtlelab6x import turtle,home,library,shop,check
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

route1 = check_route(library.x,library.y,turtle.x,turtle.y) + check_route(shop.x,shop.y,library.x,library.y) + check_route(home.x,home.y,shop.x,shop.y)
route2 = check_route(shop.x,shop.y,turtle.x,turtle.y) + check_route(library.x,library.y,shop.x,shop.y) + check_route(home.x,home.y,library.x,library.y)
if route1 < route2:
    walkto(library.x,library.y)
    walkto(shop.x,shop.y)
else:
    walkto(shop.x,shop.y)
    walkto(library.x,library.y)
walkto(home.x,home.y)


check()
