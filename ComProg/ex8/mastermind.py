import random


class Game:
    def __init__(self):
        '''Initialize the randomize number'''
        self.__ball = self.__add_balls()

    def __add_balls(self):
        '''Start random the number in four digits'''
        list_ball = []
        for i in range(4):
            list_ball.append(str(random.randint(1, 6)))
        return list_ball

    def check(self, guess):
        '''Check the answer from player'''
        correct = ""
        checked = []
        ball = list(self.__ball)
        guess = list(guess)
        for i in range(len(guess)):
            if guess[i] == ball[i]:
                correct += "*"
                checked.append(guess[i])
                ball[i] = '-'
                guess[i] = '='
        guess = list(set(guess))
        for i in range(len(guess)):
            for j in range(len(ball)):
                if guess[i] == ball[j]:
                    correct += "o"
                    ball[j] = '-'
                    break
        return correct
