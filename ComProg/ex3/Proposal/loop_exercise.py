def fib(n):
    """This function prints a Fibonacci sequence up to the nth Fibonacci
    """
    number = 1
    previous = 0
    for i in range(n + 1):
        print(number, end="  ")
        temp = number
        number += previous
        previous = temp


print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    print("")
    n += 1


def diamond(n):
    """This function prints a diamond shape of size n as shown in loop_exercise_result.txt
    """
    for i in range(n):
        for j in range(n - i, 0, -1):
            print(" ", end="")
        for j in range(i + 1):
            print("**", end="")
        print("")
    for i in range(n):
        for j in range(i + 1):
            print(" ", end="")
        for j in range(n - i):
            print("**", end="")
        print("")


print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")


def hailstone(n):
    """This function prints a hailstone sequence whose details can be found in this link:
        http://mathworld.wolfram.com/CollatzProblem.html
    """

    while n != 1:
        print(int(n), end="  ")
        if n % 2 == 0:
            n = (1 / 2) * n
        else:
            n = 3 * n + 1
    print("1", end="")


print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")


def arith_sum(n):
    """This function prints the arithmetic sequence starting from 1 to nth together with its sum
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if i > 1:
            print("+", end=" ")
        print(f"{i}", end=" ")
    print(f"= {sum}", end="")


print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("")
