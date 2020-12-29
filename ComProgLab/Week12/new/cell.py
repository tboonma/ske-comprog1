class Cell:
    def __init__(self, cell_id, move, hold):
        self.__id = cell_id
        self.__move = move
        self.__hold = hold
        self.__occupy_list = []

    def get_occupy_list_str(self):
        output = ""
        for i in self.__occupy_list:
            output += "{},".format(i.name)
        last_chr = len(output)
        if last_chr > 0 :
            output = output[:last_chr-1]
        return output
    
    def add_occupy_list(self, player):
        occupy_list = self.__occupy_list
        occupy_list.append(player)

    def remove_occupy_list(self, player):
        self.__occupy_list.remove(player)

    @property
    def move(self):
        return self.__move

    @property
    def hold(self):
        return self.__hold

    @property
    def occupy_list(self):
        return self.__occupy_list

    def __str__(self):
        return "{},{},{}".format(self.__id, self.__move, self.__hold)