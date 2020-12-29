LAB = "turtlelab5.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.11",LAB)

from turtlelab5 import turtle,mozart,check

if mozart.x > 0:
    turtle.forward(mozart.x)
elif mozart.x < 0:
    turtle.backward(-mozart.x)
if mozart.y > 0:
    if turtle.heading == 0:
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(mozart.y)
elif mozart.y < 0:
    if turtle.heading == 0:
        turtle.right(90)
    else:
        turtle.left(90)
    turtle.forward(-mozart.y)
    
check()
