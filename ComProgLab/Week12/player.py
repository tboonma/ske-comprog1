class Player:
    def __init__(self, name, current_pos=0, current_hold=False, current_move=0):
        self.name = name
        self.__current_pos = current_pos
        self.__current_hold = current_hold
        self.__current_move = current_move
    
    def __str__(self):
        return "{}: Pos = {}: Hold = {}: Move = {}".format(self.name, self.__current_pos, self.__current_hold, self.__current_move)
    
