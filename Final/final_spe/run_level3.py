from item import *
from order import *
from stock import *
from customer import *
from factory import *

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

## Add your own code to create a list of 6 items here

factory = Factory(stock_list, item_list, 'customer_orders.txt')
factory.print_stock_list()
factory.print_item_list()
factory.print_customer_list()

## Add your own code from here