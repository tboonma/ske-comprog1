class Cell:
    def __init__(self, id, move=0, hold=True, occupy_list=[]):
        self.__id = id
        self.__move = move
        self.__hold = hold
        self.__occupy_list = []
    
    def get_occupy_list_str(self):
        output = ""
        for i in self.__occupy_list:
            output += "{},".format(i)
        return output
    
    def add_occupy_list(self, player):
        self.__occupy_list.append(player.name)

    def remove_occupy_list(self, player):
        self.__occupy_list.remove(player.name)

    def __str__(self):
        return "{},{},{}".format(self.__id, self.__move, self.__hold)