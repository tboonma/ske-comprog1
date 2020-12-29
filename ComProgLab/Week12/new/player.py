from board import Board
import random

class Player:
    def __init__(self, name):
        self.__name = name
        self.__current_pos = 0
        self.__current_hold = False
        self.__current_move = 0
    
    @property
    def name(self):
        return self.__name
    
    @property
    def current_move(self):
        return self.__current_move
    
    @property
    def current_pos(self):
        return self.__current_pos
    
    @property
    def current_hold(self):
        return self.__current_hold
    
    @current_hold.setter
    def current_hold(self, value):
        self.__current_hold = value

    @current_pos.setter
    def current_pos(self, value):
        self.__current_pos += value

    @current_move.setter
    def current_move(self, value):
            self.__current_move = value

    def move(self, board):
        self.__current_pos += self.__current_move
        if self.__current_pos > len(board.cell_list)-1:
            self.__current_pos = len(board.cell_list)-1
        self.__current_move = 0

    def obtain_cell_status(self, board):
        self.__current_move = int(board.cell_list[self.__current_pos].move)
        self.__current_hold = board.cell_list[self.__current_pos].hold

    def __str__(self):
        return "{}: Pos = {}: Hold = {}: Move = {}".format(self.name, self.__current_pos, self.__current_hold, self.__current_move)

    def randomize_dice(self):
        self.__current_move = random.randint(1,6)