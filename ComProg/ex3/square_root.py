import math

# define two global variables
y = 0
count = 0


def mysqrt(a):
    global count, y
    if count == 1 or y == 0:
        x = a // 2
        if x == 0:
            x = 1
        count = count + 1
    else:
        x = y
    y = (x + a / x) / 2
    if x == y:
        return x
    return mysqrt(a)


def test_square_root(i, ans, m, diff):
    print(f"{i:<4.1f}", end=" ")
    if len(str(ans)) > 13:
        print(f"{ans:<13.11f}", end=" ")
    else:
        print(f"{ans:<13}", end=" ")
    if len(str(m)) > 13:
        print(f"{m:<13.11f}", end=" ")
    else:
        print(f"{m:<13}", end=" ")
    if len(str(diff)) > 13:
        print(f"{diff:<13.11e}")
    else:
        print(f"{diff:<13}")


print(f"a    mysqrt(a)     math.sqrt(a)  diff")
print(f"-    ---------     ------------  ----")
for i in range(1, 10):
    ans = float(mysqrt(i))
    test_square_root(i, ans, math.sqrt(i), abs(ans - math.sqrt(i)))
