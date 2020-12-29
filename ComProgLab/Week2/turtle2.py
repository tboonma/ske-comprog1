from turtlelab5x import turtle,mickey,raph,leo,donnie,check

def moveto(x,y):
    if turtle.heading == 90:
        turtle.right(90)
    elif turtle.heading == 180:
        turtle.right(180)
    elif turtle.heading == 270:
        turtle.left(90)
    if x-turtle.x > 0:
        turtle.forward(x-turtle.x)  
    else:
        turtle.backward(-(x-turtle.x))
    if y-turtle.y > 0:
        turtle.left(90)
        turtle.forward(y-turtle.y)
    else:
        turtle.right(90)
        turtle.forward(-(y-turtle.y))

# main program
moveto(mickey.x,mickey.y)
moveto(raph.x,raph.y)
moveto(leo.x,leo.y)
moveto(donnie.x,donnie.y)

check()
