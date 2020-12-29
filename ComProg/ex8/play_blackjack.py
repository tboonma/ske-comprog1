from blackjack import *

loop = True
while loop:
    new_BJ = Blackjack()
    new_BJ.start()
    new_BJ.display_player_hand()
    new_BJ.display_computer_hand()

    # player plays
    while new_BJ.player_hand_status != 'can_stay' and new_BJ.player_hand_status != 'stay' and new_BJ.player_hand_status != 'dead':
        new_BJ.adjust_player_hand()
        new_BJ.display_player_hand()
    while new_BJ.player_hand_status == 'can_stay':
        more_card = input("More cards? ")
        if more_card.lower() == 'no':
            more_card = True
        else:
            more_card = False
        if more_card == False:
            new_BJ.adjust_player_hand()
            new_BJ.display_player_hand()
        else:
            new_BJ.player_hand_status = 'stay'

    # computer plays
    while new_BJ.computer_hand_status != 'can_stay' and new_BJ.computer_hand_status != 'dead' and new_BJ.computer_hand_status != 'stay' and new_BJ.player_hand_status != 'dead':
        new_BJ.adjust_computer_hand()
    while sum(new_BJ.computer_hand_value) < sum(
            new_BJ.player_hand_value) and new_BJ.computer_hand_status == 'can_stay' and new_BJ.player_hand_status != 'dead':
        new_BJ.adjust_computer_hand()
    new_BJ.display_computer_hand()

    new_BJ.decision()

    loop_ask = input("Play a new round: ")
    if 'no' in loop_ask.lower():
        loop = False
    print()
