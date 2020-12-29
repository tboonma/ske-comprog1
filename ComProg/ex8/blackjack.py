from card_deck import *


class Blackjack:
    '''This class describes the game of Blackjack itself 
    '''

    def __init__(self):
        deck = CardDeck()
        deck.shuffle()
        self.bj_deck = deck
        self.player_hand = []
        self.computer_hand = []
        self.player_hand_value = []  # can have multiple values when hand involves Aces
        self.computer_hand_value = []  # can have multiple values when hand involves Aces
        self.player_hand_status = ''  # [stay or dead or can_stay or must_draw_more]
        self.computer_hand_status = ''  # [stay or dead or can_stay or must_draw_more]

    def start(self):
        '''This method starts the game by drawing from the card deck 
        (represented by self.bj_deck) two cards for player and two cards 
        for computer; then it proceed to update all the values and statuses for both hands
        >>> b = Blackjack()
        >>> b.start()
        Let's play Blackjack!
        '''
        print("Let's play Blackjack!")
        for i in range(2):
            self.adjust_player_hand()
            self.adjust_computer_hand()

    def adjust_player_hand(self):
        '''This method draws an additional card and reevalute the value and status 
        of the player hand
        '''
        card_draw = self.bj_deck.draw_cards(1)
        self.player_hand += card_draw
        if card_draw[0][0] == 'J' or card_draw[0][0] == 'Q' or card_draw[0][0] == 'K' or card_draw[0][0] == '1':
            self.player_hand_value.append(10)
        elif card_draw[0][0] != 'A':
            self.player_hand_value.append(int(card_draw[0][0]))
        else:
            if sum(self.player_hand_value) <= 10:
                self.player_hand_value.append(11)
            else:
                self.player_hand_value.append(1)
        if sum(self.player_hand_value) > 21 and 11 in self.player_hand_value:
            self.player_hand_value.remove(11)
            self.player_hand_value.append(1)
        if sum(self.player_hand_value) < 16:
            self.player_hand_status = 'must_draw_more'
        elif sum(self.player_hand_value) < 21:
            self.player_hand_status = 'can_stay'
        elif sum(self.player_hand_value) == 21:
            self.player_hand_status = 'stay'
        else:
            self.player_hand_status = 'dead'

    def adjust_computer_hand(self):
        '''This method draws an additional card and reevalute the value and status of the
        computer hand
        '''
        card_draw = self.bj_deck.draw_cards(1)
        self.computer_hand += card_draw
        if card_draw[0][0] == 'J' or card_draw[0][0] == 'Q' or card_draw[0][0] == 'K' or card_draw[0][0] == '1':
            self.computer_hand_value.append(10)
        elif card_draw[0][0] != 'A':
            self.computer_hand_value.append(int(card_draw[0][0]))
        else:
            if sum(self.computer_hand_value) <= 10:
                self.computer_hand_value.append(11)
            else:
                self.computer_hand_value.append(1)
        if sum(self.computer_hand_value) > 21 and 11 in self.computer_hand_value:
            self.computer_hand_value.remove(11)
            self.computer_hand_value.append(1)
        if sum(self.computer_hand_value) < 16:
            self.computer_hand_status = 'must_draw_more'
        elif sum(self.computer_hand_value) < 21:
            self.computer_hand_status = 'can_stay'
        elif sum(self.computer_hand_value) == 21:
            self.computer_hand_status = 'stay'
        else:
            self.computer_hand_status = 'dead'

    def display_player_hand(self):
        '''This method reveals the player hand'''
        SUITS_sym = ["\u2663", "\u2666", "\u2660", "\u2665"]
        print("Your hand:", end=" ")
        for card in self.player_hand:
            print(f'{card[0]}', end='')
            if card[0] == '1':
                print(f'{card[1]}', end='')
            if 'Clubs' in card:
                print(f'{SUITS_sym[0]}', end=' ')
            elif 'Diamonds' in card:
                print(f'{SUITS_sym[1]}', end=' ')
            elif 'Spades' in card:
                print(f'{SUITS_sym[2]}', end=' ')
            elif 'Hearts' in card:
                print(f'{SUITS_sym[3]}', end=' ')
        print()

    def display_computer_hand(self):
        '''This method reveals the computer hand '''
        SUITS_sym = ["\u2663", "\u2666", "\u2660", "\u2665"]
        print("Computer hand:", end=" ")
        for card in self.computer_hand:
            print(f'{card[0]}', end='')
            if card[0] == '1':
                print(f'{card[1]}', end='')
            if 'Clubs' in card:
                print(f'{SUITS_sym[0]}', end=' ')
            elif 'Diamonds' in card:
                print(f'{SUITS_sym[1]}', end=' ')
            elif 'Spades' in card:
                print(f'{SUITS_sym[2]}', end=' ')
            elif 'Hearts' in card:
                print(f'{SUITS_sym[3]}', end=' ')
            if self.player_hand_status == 'must_draw_more' or self.player_hand_status == 'can_stay':
                break
        print()

    def decision(self):
        '''This method makes a decision if the player wins, looses, or ties with the
        computer 
        '''
        if self.player_hand_status == 'dead':
            self.player_hand_value = [0]
        if self.computer_hand_status == 'dead':
            self.computer_hand_value = [0]
        if sum(self.player_hand_value) > sum(self.computer_hand_value):
            print('You win!')
        elif sum(self.player_hand_value) < sum(self.computer_hand_value):
            print('You loose!')
        else:
            print('You tie with the computer!')


if __name__ == "__main__":
    import doctest

    doctest.testmod()
