import math


def check_unit(ans):
    """Check plural (square meter or square meters)"""
    if ans > 1:
        return "square meters"
    else:
        return "square meter"

def cal_circle(r):
    """Calculate and return area result)"""
    return math.pi*r*r

def cal_triangle(b,h):
    """Calculate and return area result)"""
    return (1/2)*b*h

def cal_rectangle(w,h):
    """Calculate and return area result)"""
    return w*h

def print_result(atype,ans,unit):
    """Print the area result with correct unit(s)"""
    print(f'Area of this {atype} is {ans:.2f} {unit}.')


def check_float_input(msg):
    """Loop until a correct float number is entered then return"""
    num = ["1","2","3","4","5","6","7","8","9","0","."]
    while True:
        again = False
        x = input(msg)
        for j in x:
            if j in num:
                continue
            else:
                again = True
                break
        if again:
            print("Please enter a number!")
        else:
            break
    return float(x)
while True:
    action = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ").lower()
    if action == 't':
        base = check_float_input("base = ")
        height = check_float_input("height = ")
        ans = cal_triangle(base, height)
        print_result("triangle", ans, check_unit(ans))
    elif action == 'r':
        width = check_float_input("width = ")
        height = check_float_input("height = ")
        ans = cal_rectangle(width, height)
        print_result("rectangle", ans, check_unit(ans))
    elif action == 'c':
        radius = check_float_input("Radius = ")
        ans = cal_circle(radius)
        print_result("circle", ans, check_unit(ans))
    elif action == 'q':
        print("Bye")
        break
    else:
        print("Incorrect Input")
        continue

