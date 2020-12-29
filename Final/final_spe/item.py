class Item:
    def __init__(self, item_id, item_type, item_color):
        self.__id = item_id
        self.__type = item_type
        self.__color = item_color
    
    @property
    def item_id(self):
        return self.__id
    
    @property
    def item_type(self):
        return self.__type
    
    @property
    def item_color(self):
        return self.__color
    
    def __eq__(self, other):
        if self.__id == other.__id:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__id},{self.__type},{self.__color}"