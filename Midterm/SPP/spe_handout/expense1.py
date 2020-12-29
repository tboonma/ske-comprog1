def compare_nums(number1, number2):
    if number1 < number2:
        return "less than"
    elif number1 > number2:
        return "more than"
    else:
        return "equal to"


def read_list(n):
    expense_list = []
    for i in range(n):
        expense = float(input(f"Day {i + 1}: enter expense: "))
        expense_list.append(expense)
    return expense_list


def print_list_comparison(expense1, expense2):
    for i in range(len(expense1)):
        print(f"Day {i + 1}: Teacher1 spends {compare_nums(expense1[i], expense2[i])} Teacher2 ")
    pass


# level 1.1
# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
# print(f"{x} is {compare_nums(x,y)} {y}")

# level 1.2
days = int(input("Enter #days: "))
print("Teacher 1:")
teacher1_expense = read_list(days)
print("Teacher 2:")
teacher2_expense = read_list(days)
print(f"{teacher1_expense}\n{teacher2_expense}")
print_list_comparison(teacher1_expense, teacher2_expense)
