def is_triangle(a,b,c):
    if a+b>c:
        if a+c>b:
            if b+c>a:
                return True
    return False

def right_triangle(a,b,c):
    if a**2 == b**2 + c**2:
        return True
    elif b**2 == a**2 + c**2:
        return True
    elif c**2 == a**2 + b**2:
        return True
    else:
        return False
a = float(input("Enter 1st line's length: "))
b = float(input("Enter 2nd line's length: "))
c = float(input("Enter 3rd line's length: "))
if is_triangle(a,b,c):
    if right_triangle(a,b,c):
        print("It's a right triangle.")
    else:
        print("It's a triangle but not a right triangle.")
else:
    print("It's not a triangle.")