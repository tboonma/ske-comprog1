def print_hello():
    name = input("Input name :")
    print(f"Hello,{name}")

print_hello()

def read_one_int(msg):
    number = int(input(msg))
    return number

read_one_int()

num = read_one_int()
num2 = read_one_int()
print(num+num2)

num = read_one_int("Enter num :")
num2 = read_one_int("Enter num2 :")
print(num+num2)

def read_two_floats():
