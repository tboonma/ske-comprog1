def read_file(filename):
    f = open(filename, "r")
    data = f.read().split('\n')
    for i in range(len(data)):
        if data[i] == '':
            data.pop(i)
        else:
            data[i] = float(data[i])
    return data


def read_menu_choice():
    print(r"""
Menu:
1=List comparison
2=Partial sum
3=Find max
0=Quit""")
    action = int(input("Enter your choice: "))
    return action


def compare_nums(number1, number2):
    if number1 < number2:
        return "less than"
    elif number1 > number2:
        return "more than"
    else:
        return "equal to"


def print_list_comparison(expense1, expense2):
    for i in range(len(expense1)):
        print(f"Day {i + 1}: Teacher1 spends {compare_nums(expense1[i], expense2[i])} Teacher2 ")
    pass


def read_day_list():
    day_received = []
    while True:
        day_number = int(input("Enter day number: "))
        if day_number != -99:
            day_received.append(day_number)
        else:
            break
    return day_received


def compute_partial_sum(days):
    sum = 0
    for i in days:
        sum += teacher_list[i - 1]
    return sum


def find_max(expense):
    max_expense = max(expense)
    day = expense.index(max_expense) + 1
    return day, max_expense


data_set = input('Enter your data set (A,B,C): ')
filename1 = 'teacher1' + data_set + '.txt'
filename2 = 'teacher2' + data_set + '.txt'
t1 = read_file(filename1)
t2 = read_file(filename2)
print(f"Teacher 1:\n{t1}")
print(f"Teacher 2:\n{t2}")
while True:
    action = read_menu_choice()
    if action == 1:
        print_list_comparison(t1, t2)
    elif action == 2:
        while True:
            print("Compute sum of some days...")
            days = read_day_list()
            teacher = int(input("Which teacher (1 or 2): "))
            print(days)
            if teacher == 1:
                teacher_list = t1
            elif teacher == 2:
                teacher_list = t2
            print(teacher_list)
            print(f"Sum of Days {days} = {compute_partial_sum(days):.2f}")
            cont = input("Continue (y/n): ")
            if cont == 'n':
                break
            print("")
    elif action == 3:
        teacher = int(input("Which teacher (1 or 2): "))
        if teacher == 1:
            day, amount = find_max(t1)
            print(f"Teacher1 spends maximum money = {amount:.2f} on Day{day}")
        elif teacher == 2:
            day, amount = find_max(t2)
            print(f"Teacher2 spends maximum money = {amount:.2f} on Day{day}")
    elif action == 0:
        break
