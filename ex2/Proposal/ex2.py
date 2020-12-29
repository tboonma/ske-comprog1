# Exercise 2
# import instant function
from math import sqrt

# First program
# input two values as a string
spin = input("Spin: ")
charge = input("Charge: ")

# Check and print particle and class by compare two strings
if spin == "1/2":
    if charge == "-1/3":
        print("Strange Quark")
    elif charge == "2/3":
        print("Charm Quark")
    elif charge == "-1":
        print("Electron Lepton")
    elif charge == "0":
        print("Neutrino Lepton")
    else:
        print("Error")
elif spin == "1":
    if charge == "0":
        print("Photon Boson")
    else:
        print("Error")

# Second program
# input two number and operation
first_number = float(input("First number : "))
second_number = float(input("Second number : "))
operation = input("Operation : ")

# check the operation and calculate
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "pow":
    print(first_number ** second_number)
elif operation == "/":
    if second_number != 0:  # Check second number is not zero
        print(first_number / second_number)
    else:
        print("Division by 0!")
elif operation == "mod":
    if second_number != 0:  # Check second number is not zero
        print(first_number % second_number)
    else:
        print("Division by 0!")
elif operation == "div":
    if second_number != 0:  # Check second number is not zero
        print(first_number // second_number)
    else:
        print("Division by 0!")
else:
    print("Error: operation invalid")

# Third program
# input user's money
money = int(input("Your money: "))

# define each animal price
chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

# set how many animals the user can afford to zero
quantity = 0

# name the animal to none
animal_name = "None"

# set change equal to money
change = money

# calculate the maximum animals the user can afford by mod
if money % chicken_price < change:
    quantity = money // chicken_price
    animal_name = "chicken"
if money % goat_price < change:
    quantity = money // goat_price
    animal_name = "goat"
if money % pig_price < change:
    quantity = money // pig_price
    animal_name = "pig"
if money % cow_price < change:
    quantity = money // cow_price
    animal_name = "cow"
if money % sheep_price < change:
    quantity = money // sheep_price
    animal_name = "sheep"

# print the result
if animal_name == "None":  # check if there is no animal that user can afford
    print("None")
elif animal_name == "sheep":  # check if the result is sheep that is irregular plural
    print(f"{quantity} sheep")
else:
    if quantity == 1:
        print(f"{quantity} {animal_name}")
    else:
        print(f"{quantity} {animal_name}s")

# Fourth program
# define the reference time point to Tuesday, 10:30 in the morning in London (UTC+00:00)
ref_time = 10 + (30 / 60)

# get user offset for some time zone.
offset = int(input("Offset: "))

# calculate the user's time
user_time = ref_time + offset

# check and print user's date of week
if user_time > 24:
    print("Wednesday")
elif user_time < 0:
    print("Monday")
else:
    print("Tuesday")

# Fifth program
# create function is_even to check if number is even
def is_even(num):
    if num % 2 == 0:
        return "True"
    else:
        return "False"

# get number from user
number = int(input("Number : "))

# calculate user's number in function
if is_even(number):
    print(is_even(number))

# sixth program
# create function is_leap_year to check if year is a leap
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        else:
            return "True"
    else:
        return "False"


# get a year from user
year = int(input("Input year : "))

# go to function is_leap_year and print the result
print(is_leap_year(year))


# seventh program
# create function interval_intersect to check the intersect
def interval_intersect(a, b, c, d):
    if c <= b and c >= a or d >= a and d <= b:
        return "True"
    elif a >= c and a <= d or b >= c and b <= d:
        return "True"
    else:
        return "False"

# Input four parameters from user
a = int(input("Input a : "))
b = int(input("Input b : "))
c = int(input("Input c : "))
d = int(input("Input d : "))

# go to function interval_intersect
print(interval_intersect(a, b, c, d))

# eighth program
# create function print_digits to check the digits
def print_digits(num):
    if len(num) > 2:  # check if length of number more than two digits
        print("Error: Input is not a two- digit number.")
    elif len(num) == 1:
        print(f"The tens digit is 0 and the ones digits is {num[0]}")
    else:
        print(f"The tens digit is {num[0]} and the ones digits is {num[1]}")

# input two digits integer from user
number = input("Input number : ")

# go to print_digits
print_digits(number)

# ninth program
# create function smaller_root to return the smallest solution
def smaller_root(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0 or a == b == c == 0:
        return "Error: No real solutions"
    elif discriminant == 0:
        x = (-b) / (2 * a)
        return x
    elif discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        if x1 < x2:
            return x1
        else:
            return x2

# get the equation from user
a = int(input("input a : "))
b = int(input("input b : "))
c = int(input("input c : "))

# go to function smaller_root to solve the equation
print(smaller_root(a, b, c))


# tenth program
# create function there_is_odd to check if there is odd integer
def there_is_odd(x, y, z):
    num = ""
    if x % 2 != 0:
        num = num + " " + str(x)
    if y % 2 != 0:
        num = num + " " + str(y)
    if z % 2 != 0:
        num = num + " " + str(z)
    print(f"There is an odd number whose value is{num}")


# get three integers from user
x = int(input("Input x : "))
y = int(input("Input y : "))
z = int(input("Input z : "))

# go to there_is_odd function and print the result
there_is_odd(x, y, z)


# eleventh program
# create function list_all_odds to print the odd integer
def list_all_odds(w, x, y, z):
    if w % 2 != 0:
        print(f"This value is odd: {w}")
    if x % 2 != 0:
        print(f"This value is odd: {x}")
    if y % 2 != 0:
        print(f"This value is odd: {y}")
    if z % 2 != 0:
        print(f"This value is odd: {z}")
    if w % 2 == x % 2 == y % 2 == z % 2 == 0:
        print("There is no odd number")

# get four values from user
w = int(input("Input 1st number: "))
x = int(input("Input 2nd number: "))
y = int(input("Input 3rd number: "))
z = int(input("Input 4th number: "))

# go to function to check the odd number
list_all_odds(w, x, y, z)


# twelfth program
# create max_of_three function to find the max integer
def max_of_three(x, y, z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max


# get three integers from user
x = int(input("Input 1st number: "))
y = int(input("Input 2nd number: "))
z = int(input("Input 3rd number: "))

# go to max_of_three to find and print the max value
print(f"The max value is {max_of_three(x, y, z)}")
