water, milk, coffee_beans, cups, money = 400, 540, 120, 9, 550  # define value for each ingradients


def print_coffee():  # print ingredients remaining
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{money} of money""")


def make_coffee(w, mi, co, mo):
    global water, milk, coffee_beans, cups, money
    temp_w, temp_mi, temp_co, temp_cu, temp_mo = water, milk, coffee_beans, cups, money
    empty = ""
    if water - w >= 0:
        water -= w
    else:
        empty = "water"
    if milk - mi >= 0:
        milk -= mi
    else:
        if empty:
            empty += "milk"
        else:
            empty += ", milk"
    if coffee_beans - co >= 0:
        coffee_beans -= co
    else:
        if empty:
            empty += "coffee beans"
        else:
            empty += ", coffee beans"
    if cups - 1 >= 0:
        cups -= 1
    else:
        if empty:
            empty += "cups"
        else:
            empty += ", cups"
    if empty:
        water, milk, coffee_beans, cups, money = temp_w, temp_mi, temp_co, temp_cu, temp_mo
        return empty
    else:
        money += mo


while True:
    action = input("Write action (buy, fill, take, remaining, exit)\n> ")  # get operation from user
    if action == "buy":
        print("")
        type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")
        if type == "1":
            check = make_coffee(250, 0, 16, 4)
            if check:
                print(f"Sorry, not enough {check}!")
            else:
                print("I have enough resources, making you a coffee!")
        elif type == "2":
            check = make_coffee(350, 75, 20, 7)
            if check:
                print(f"Sorry, not enough {check}!")
            else:
                print("I have enough resources, making you a coffee!")
        elif type == "3":
            check = make_coffee(200, 100, 12, 6)
            if check:
                print(f"Sorry, not enough {check}!")
            else:
                print("I have enough resources, making you a coffee!")
        elif type == "back":
            continue
    elif action == "fill":
        print("")
        water = water + int(input("Write how many ml of water do you want to add:\n> "))
        milk = milk + int(input("Write how many ml of milk do you want to add:\n> "))
        coffee_beans = coffee_beans + int(input("Write how many grams of coffee beans do you want to add:\n> "))
        cups = cups + int(input("Write how many disposable cups of coffee do you want to add:\n> "))
    elif action == "take":
        print(f"\nI gave you ${money}")
        money = 0
    elif action == "remaining":
        print_coffee()
    elif action == "exit":
        break
    print("")
