from item import *
from order import *
from stock import *
from customer import *

# Copy 4 functions from Level 1 here:
# print_stock_list, print_item_list, print_order_list, process_order_list
def print_stock_list(stock_list):
#   fill your own code for print_stock_list
    print("Stock List:")
    for stock in stock_list:
        print(stock)

def print_item_list(item_list):
#   fill your own code for print_item_list
    print("Item List:")
    for item in item_list:
        print(item)

def print_order_list(order_list):
#    fill your own code for print_order_list
    for order in order_list:
        print(order)

def process_order_list(customer, stock_list):
#    fill your own code for process_order_list
    order_list = customer.order_list
    for order in order_list:
        if order.amount <= stock_list[order.item.item_id - 1].amount:
            stock_list[order.item.item_id - 1].amount -= order.amount
            order.cost = stock_list[order.item.item_id - 1].price * order.amount
            order.status = 'Delivered'
            customer.compute_total_cost(order.cost)
        else:
            order.status = 'Insufficient'

item1 = Item(1,'T-shirt', 'White')
item2 = Item(2,'T-shirt', 'Black')
item3 = Item(3,'Polo-shirt', 'White')
item4 = Item(4,'Polo-shirt', 'Green')
item5 = Item(5,'Shirt', 'Green')
item6 = Item(6,'Shirt', 'Black')

stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)

## Add your own code to create a list of stocks here
stock_list = [stock1, stock2, stock3, stock4, stock5, stock6]
print_stock_list(stock_list)

## Add your own code to create a list of 6 items here
item_list = [item1, item2, item3, item4, item5, item6]
print_item_list(item_list)


## Add your own code to create a list of customers
## Hint: For each customer, you need to read two things from user: 1) name and 2) order_list
## After reading information of each customer, create and print this customer, append each customer to a list of customers
all_customers = []
number = 1
while True:
    print()
    print(f"Customer #{number}")
    name = input("Enter name of customer: ")
    order_list = []
    while True:
        item_id = int(input("Enter item id (negative to quit): "))
        if item_id < 0:
            break
        amount = int(input("Enter amount: "))
        order_list.append(Order(item_list[item_id-1], amount))
    all_customers.append(Customer(name, order_list))
    print(f"Customer: {name}")
    print(f"Total_cost = 0")
    print_order_list(order_list)
    action = input("\nContinue to read new customer (y/n): ")
    if action.lower() == 'n':
        break
    number += 1



## In the list of customers, process order list of each customer
for customer in all_customers:
    process_order_list(customer, stock_list)
## After processing order list of all customers, print information of each customer
for customer in all_customers:
    print(f"Customer: {customer.name}")
    print(f"Total_cost = {customer.total_cost}")
    for order in customer.order_list:
        print(order)
    print()

print_stock_list(stock_list)





