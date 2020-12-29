from card_deck import *

class Player:
    def __init__(self, name):
        self.__name = name
        self.__hand = []
        self.__value = []
        self.__status = ''
        self.__score = 0
    
    @property
    def name(self):
        return self.__name

    @property
    def hand(self):
        return self.__hand
    
    @hand.setter
    def hand(self, value):
        self.__hand = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value
    
    @property
    def score(self):
        return self.__score
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value
    
    def adjust_hand(self, card_draw):
        self.__hand += card_draw
        if card_draw[0][0] == 'J' or card_draw[0][0] == 'Q' or card_draw[0][0] == 'K' or card_draw[0][0] == '1':
            self.__value.append(10)
        elif card_draw[0][0] != 'A':
            self.__value.append(int(card_draw[0][0]))
        else:
            if sum(self.__value) <= 10:
                self.__value.append(11)
            else:
                self.__value.append(1)
        if sum(self.__value) > 21 and 11 in self.__value:
            self.__value.remove(11)
            self.__value.append(1)
        if sum(self.__value) < 16:
            self.__status = 'must_draw_more'
        elif sum(self.__value) < 21:
            self.__status = 'can_stay'
        elif sum(self.__value) == 21:
            self.__status = 'stay'
        else:
            self.__status = 'dead'

    def update_score(self, value):
        self.__score += value