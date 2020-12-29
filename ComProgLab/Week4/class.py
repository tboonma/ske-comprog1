def read_one_float(msg):
    num = float(input(msg))
    return num


def read_two_floats():
    side1 = read_one_float("Enter side1: ")
    side2 = read_one_float("Enter side2: ")
    return side1, side2


def compute_rectangle_area(side1, side2):
    return side1 * side2


def compute_rectangle_perimeter(side1, side2):
    return (side1 + side2) * 2


a, b = read_two_floats()
action = input("Area (A) or Perimeter (P)? ")
if action == 'a' or action == 'A':
    print(f"Area is {compute_rectangle_area(a, b):.2f}")
elif action == 'p' or action == 'P':
    print(f"Perimater is {compute_rectangle_perimeter(a, b):.2f}")
