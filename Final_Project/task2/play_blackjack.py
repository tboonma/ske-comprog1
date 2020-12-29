from blackjack import *
from player import *

new_BJ = Blackjack()
num_players = int(input("How many players to deal? "))
for i in range(num_players):
    new_BJ.add_player("Player " + str(i))
while True:
    new_BJ.start()
    for i in range(num_players):
        new_BJ.display_player_hand(i)
    new_BJ.display_computer_hand()
    # player plays
    for i in range(num_players):
        print()
        displayed = False
        while new_BJ.player[i].status != 'can_stay' and new_BJ.player[i].status != 'stay' and new_BJ.player[i].status != 'dead':
            new_BJ.adjust_player_hand(i)
            new_BJ.display_player_hand(i)
            displayed = True
        if not displayed:
            new_BJ.display_player_hand(i)
        while new_BJ.player[i].status == 'can_stay':
            more_card = input("More cards? ")
            if more_card.lower() == 'no':
                more_card = True
            else:
                more_card = False
            if more_card == False:
                new_BJ.adjust_player_hand(i)
                new_BJ.display_player_hand(i)
            else:
                new_BJ.player[i].status = 'stay'
    # computer plays
    print()
    all_value = new_BJ.check_all_player_value()
    displayed = False
    while new_BJ.computer_hand_status != 'can_stay' and new_BJ.computer_hand_status != 'dead' and new_BJ.computer_hand_status != 'stay':
        new_BJ.adjust_computer_hand()
        new_BJ.display_computer_hand()
        displayed = True
    while new_BJ.computer_hand_status == 'can_stay':
        for i in all_value:
            if sum(new_BJ.computer_hand_value) > i:
                new_BJ.computer_hand_status = 'stay'
                break
        if new_BJ.computer_hand_status != 'can_stay':
            break
        new_BJ.adjust_computer_hand()
        new_BJ.display_computer_hand()
        displayed = True
    if not displayed:
        new_BJ.display_computer_hand()
    new_BJ.decision()
    loop_ask = input("\nNext round? ")
    if 'no' in loop_ask.lower():
        break
    new_BJ.clear()
    print()