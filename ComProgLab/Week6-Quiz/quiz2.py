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
else:
    print("Incorrect Input")
    continue
