class Order:
    def __init__(self, item, amount, cost=0):
        self.__item = item
        self.__status = 'To process'
        self.__amount = amount
        self.__cost = cost

    @property
    def amount(self):
        return self.__amount
    
    @property
    def item(self):
        return self.__item
    
    @property
    def cost(self):
        return self.__cost
    
    @cost.setter
    def cost(self, value):
        self.__cost = value
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value

    def __str__(self):
        return f"({self.__item.item_id},{self.__item.item_type},{self.__item.item_color},{self.__amount},{self.__cost} Baht,{self.__status})"