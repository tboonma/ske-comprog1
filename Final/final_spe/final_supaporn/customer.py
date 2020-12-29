class Customer:
    def __init__(self, name, order_list):
        self.__name = name
        self.__order_list = order_list
        self.__total_cost = 0
    
    @property
    def name(self):
        return self.__name
    
    @property
    def order_list(self):
        return self.__order_list
    
    @property
    def total_cost(self):
        return self.__total_cost
    
    def compute_total_cost(self, value):
        self.__total_cost += value

