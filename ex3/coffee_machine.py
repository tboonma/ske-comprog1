water, milk, coffee_beans, cups, money = 400, 540, 120, 9, 550  # define value for each ingradients


def print_coffee():  # print ingredients remaining
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{money} of money
""")


print_coffee()  # print initial ingredients
action = input("Write action (buy, fill, take)\n> ")  # get operation from user
if action == "buy":
    type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> "))
    if type == 1:
        water, coffee_beans, money = water - 250, coffee_beans - 16, money + 4
    elif type == 2:
        water, milk, coffee_beans, money = water - 350, milk - 75, coffee_beans - 20, money + 7
    elif type == 3:
        water, milk, coffee_beans, money = water - 200, milk - 100, coffee_beans - 12, money + 6
elif action == "fill":
    water = water + int(input("Write how many ml of water do you want to add:\n> "))
    milk = milk + int(input("Write how many ml of milk do you want to add:\n> "))
    coffee_beans = coffee_beans + int(input("Write how many grams of coffee beans do you want to add:\n> "))
    cups = cups + int(input("Write how many disposable cups of coffee do you want to add:\n> "))
elif action == "take":
    print(f"I gave you ${money}")
    money = 0
print_coffee()  # print summary
