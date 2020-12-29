import random

class Player:
    def __init__(self, name='None', win=0, play=0, hand='None'):
        self.__name = name
        self.__num_wins = win
        self.__num_plays = play
        self.hand = hand
        self.surname = 'Johny'

    def set_name(self, name):
        self.__name = name
    
    def set_num_wins(self, num_wins):
        self.__num_wins = num_wins

    def get_num_wins(self):
        return self.__num_wins

    def get_name(self):
        return self.__name

    @property
    def num_plays(self):
        return self.__num_plays
    
    @num_plays.setter
    def num_plays(self, value):
        self.__num_plays = value

    def randomize_hand(self):
        hand_num = random.randint(1,3)
        if hand_num == 1:
            self.hand = 'Rock'
        elif hand_num == 2:
            self.hand = 'Paper'
        elif hand_num == 3:
            self.hand = 'Scissors'
        else:
            self.hand = 'Error {0}'.format(hand_num)


    def __str__(self):
        return "{0}: Wins = {1}: Plays = {2}: Hand = {3}".format(self.__name, self.__num_wins, self.__num_plays, self.hand)