# Sample output 1
t1 = [50, 20, 30]
t2 = [40, 25, 15.5]

# Sample output 2
# t1 = [40,40,50,15,12.5]
# t2 = [25,40,80,20,10]

print('Teacher 1:')
print(t1)
print('Teacher 2:')
print(t2)


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
