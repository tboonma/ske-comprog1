# first program
FEET_IN_MILE = 5280
miles = 13
feet = FEET_IN_MILE * miles
print(feet)

# second program
hours = 7
minutes = 21
seconds = 37
total = hours*3600 + minutes*60 + seconds
print(f"{hours} hours {minutes} minutes {seconds} seconds is corresponding to {total} seconds")

# third program
width = 4
height = 7
print(f"The length of the perimeter is {2*width + 2*height}")

# fourth program
PI = 3.14
radius = 8
area = PI*(radius**2)
print(f"The area of the circle is {area}")

# fifth program
present_value = 1000
annual_rate = 7
years = 10
future_value = present_value*((1+0.01*annual_rate)**years)
print(future_value)

# sixth program
from math import sqrt
x0 = 2
y0 = 2
x1 = 5
y1 = 6
distance = sqrt(((x0-x1)**2)+((y0-y1)**2))
print(distance)

# seventh program
from math import sqrt
x0 = 1
y0 = 1
x1 = 4
y1 = 1
x2 = 4
y2 = 5
a = sqrt(((x0-x1)**2)+((y0-y1)**2))
b = sqrt(((x0-x2)**2)+((y0-y2)**2))
c = sqrt(((x1-x2)**2)+((y1-y2)**2))
s = 0.5*(a+b+c)
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(area)

# eighth program
print("Write how many cups of coffee you will need:")
cups = int(input(">"))
print(f"For {cups} cups of coffee you will need:")
water = 200*cups
milk = 50*cups
coffee_beans = 15*cups
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{coffee_beans} g of coffee beans")
