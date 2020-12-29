import math


def check_unit(x):
    """Check plural (square meter or square meters)"""
    if x > 1:
        return "square meters"
    else:
        return "square meter"

def cal_circle(r):
    """Calculate and return area result)"""
    return math.pi * r * r

def cal_triangle(x,y):
    """Calculate and return area result)"""
    return (1 / 2) * x * y

def cal_rectangle(x,y):
    """Calculate and return area result)"""
    return x * y

def print_result(msg, value, unit):
    """Print the area result with correct unit(s)"""
    print(f'Area of this {msg} is {value:.2f} {unit}')


menu = input("(T)riangle (R)ectangle (C)ircle : ")
if menu == "T" or menu == "t":
    base = float(input("base = "))
    height = float(input("height = "))
    value = cal_triangle(base, height)
    unit = check_unit(value)
    print_result("triangle",value, unit)
elif menu == "R" or menu == "r":
    w = float(input("width = "))
    h = float(input("height = "))
    value = cal_rectangle(w, h)
    unit = check_unit(value)
    print_result("rectangle",value, unit)
elif menu == "C" or menu == "c":
    r = float(input("Radius = "))
    value = cal_circle(r)
    unit = check_unit(value)
    print_result("circle", value, unit)
else:
    print("Incorrect Input!")