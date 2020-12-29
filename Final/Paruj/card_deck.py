class CardDeck:
    def __init__(self):
        SUITS = [1, 2, 3, 4]
        RANKS = [i for i in range(2,15)]
        deck = []
        for rank in RANKS:
            for suit in SUITS:
                card = str(rank) + ' ' + str(suit)
                deck += [card]
        self.card_deck = deck
    
    def shuffle(self):
        import random
        n = len(self.card_deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.card_deck[r]
            self.card_deck[r] = self.card_deck[i]
            self.card_deck[i] = temp

print_card = {'11':'Jack', '12':'Queen', '13':'King', '14':'Ace'}
card_suit = ['', 'Clubs', 'Diamonds', 'Hearts', 'Spades']

p0 = 0
p1 = 0
game = CardDeck()
game.shuffle()
extract = [game.card_deck[i] for i in range(10)]
for i in range(5):
    print(f"Session {i}")
    card1 = extract[0]
    card1 = card1.split()
    card1_out = card1[0]
    if int(card1[0]) == 11:
        card1_out = 'Jack'
    elif int(card1[0]) == 12:
        card1_out = 'Queen'
    elif int(card1[0]) == 13:
        card1_out = 'King'
    elif int(card1[0]) == 14:
        card1_out = 'Ace'
    print(f"Player 0 hand: {card1_out} {card_suit[int(card1[1])]}")
    extract.pop(0)
    card2 = extract[0]
    card2 = card2.split()
    card1_out = card1[0]
    if int(card1[0]) == 11:
        card1_out = 'Jack'
    elif int(card1[0]) == 12:
        card1_out = 'Queen'
    elif int(card1[0]) == 13:
        card1_out = 'King'
    elif int(card1[0]) == 14:
        card1_out = 'Ace'
    print(f"Player 1 hand: {card1_out} {card_suit[int(card2[1])]}")
    extract.pop(0)
    if int(card1[0]) > int(card2[0]):
        print("Player 0 wins!")
    elif int(card1[0]) < int(card2[0]):
        print("Player 1 wins!")
    elif int(card1[0]) == int(card2[0]):
        if int(card1[1]) > int(card2[1]):
            print("Player 0 wins!")
        elif int(card1[1]) < int(card2[1]):
            print("Player 1 wins!")
        else:
            print("Both players tie!")
