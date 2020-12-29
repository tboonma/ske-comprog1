def print_list(x):
    for i in x:
        print(i)


def read_list(n):
    y = []
    for i in range(n):
        x = float(input(f"Input value{i + 1}: "))
        y.append(x)
    return y


def compute_area_list(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i] * y[i])
    return z


n = int(input("Enter n: "))
print("Side 1: ")
mylist1 = read_list(n)
print("Side 2: ")
mylist2 = read_list(n)
c_list = compute_area_list(mylist1, mylist2)
print_list(c_list)
