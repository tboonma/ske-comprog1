import math


def check_unit(ans):
    """Check plural (square meter or square meters)"""
    if ans > 1:
        return "square meters"
    else:
        return "square meter"


def cal_circle(r):
    """Calculate and return area result)"""
    return math.pi * r * r


def cal_triangle(b, h):
    """Calculate and return area result)"""
    return (1 / 2) * b * h


def cal_rectangle(w, h):
    """Calculate and return area result)"""
    return w * h


def print_result(atype, ans, unit):
    """Print the area result with correct unit(s)"""
    print(f'Area of this {atype} is {ans:.2f} {unit}.')
    return 0


while True:
    menu = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    if menu == 't' or menu == 'T':
        base = float(input("base = "))
        height = float(input("height = "))
        ans = cal_triangle(base, height)
        print_result("triangle", ans, check_unit(ans))
    elif menu == 'r' or menu == 'R':
        width = float(input("width = "))
        height = float(input("height = "))
        ans = cal_rectangle(width, height)
        print_result("rectangle", ans, check_unit(ans))
    elif menu == 'c' or menu == 'C':
        radius = float(input("Radius = "))
        ans = cal_circle(radius)
        print_result("circle", ans, check_unit(ans))
    elif action == 'q':
        print("Bye")
        break
    else:
        print("Incorrect Input")
