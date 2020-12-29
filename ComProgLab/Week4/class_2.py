def print_list(x):
    for i in x:
        print(i)


def read_list(n):
    y = []
    for i in range(n):
        x = float(input(f"Input value{i + 1}: "))
        y.append(x)
    return y


n = int(input("Enter n: "))
mylist = read_list(n)
print_list(mylist)
