from blackjack import *
from player import *
from player_list import *
import random

all_players = []

def read_player():
    f = open('players_info.txt', 'r')
    rows = f.read().splitlines()
    rows.pop(0)
    global all_players
    for player in rows:
        info = player.split(',')
        all_players.append(AllPlayer(info[0], info[1], info[2], info[3], info[4], info[5]))

def play():
    global all_players
    new_BJ = Blackjack()
    num_players = int(input("How many players? "))
    players = []
    for i in range(num_players):
        while True:
            select = random.choice(all_players)
            if select not in players and select.budget > 100:
                break
        players.append(select)
        new_BJ.add_player(select.name, select.budget)
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
        new_BJ.decision(all_players)
        loop_ask = input("\nNext round? ")
        if 'no' in loop_ask.lower():
            break
        new_BJ.clear()
        print()

def add_budget():
    success = False
    name = input("Enter player’s name: ")
    value = int(input("Enter added budget: "))
    for player in all_players:
        if player.name == name:
            player.budget += value
            print(f"{value} added.")
            print(f"{player.name}, {player.gender}, {player.region}")
            print(f"Budget = {player.budget}")
            print(f"Number of wins = {player.numwins}")
            print(f"Number of losses = {player.numlosses}")
            success = True
    if not success:
        print("Player not found.")

def view_profile():
    while True:
        success = False
        name = input("Enter player’s name: ")
        for player in all_players:
            if player.name == name:
                print(f"{player.name}, {player.gender}, {player.region}")
                print(f"Budget = {player.budget}")
                print(f"Number of wins = {player.numwins}")
                print(f"Number of losses = {player.numlosses}")
                success = True
        if not success:
            print("Player not found.")
        print()
        while True:
            view = input("(V)iew more profile or (B)ack to main menu: ").lower()
            if view == 'v':
                break
            if view == 'b':
                return
            else:
                print("Invalid input")
    
def view_stat():
    players = {}
    for player in all_players:
        players.update({player.name : [player.numwins, player.gender, player.region]})
    sorted_players = sorted(players.items(), key=lambda item:item[1][0], reverse=True)
    while True:
        print(r'''Stat choices:
A.Top five players with maximum number of wins
B.Top five male players with maximum number of wins
C.Top five female players with maximum number of wins
D.Top region players with maximum number of wins
E.Top region male players with maximum number of wins
F.Top region female players with maximum number of wins''')
        choice = input("\nEnter stat choice: ").lower()
        if choice == 'a':
            for i in range(5):
                print(f"{sorted_players[i][0]}, {sorted_players[i][1][0]}")
            print()
        elif choice == 'b':
            index = 0
            while True:
                if sorted_players[index][1][1] == 'M':
                    print(f"{sorted_players[index][0]}, {sorted_players[index][1][0]}")
                index += 1
                if index == 6:
                    break
            print()
        elif choice == 'c':
            index = 0
            while True:
                if sorted_players[index][1][1] == 'F':
                    print(f"{sorted_players[index][0]}, {sorted_players[index][1][0]}")
                index += 1
                if index == 6:
                    break
            print()
        elif choice == 'd':
            top = {}
            for player in sorted_players:
                if player[1][2] not in list(top.keys()):
                    top.update({player[1][2]:[player[0], player[1][1], player[1][0]]})
            for player in top:
                print(f"{player}, {top[player][0]}, {top[player][1]}, {top[player][2]}")
            print()
        elif choice == 'e':
            top = {}
            for player in sorted_players:
                if player[1][2] not in list(top.keys()) and player[1][1] == 'M':
                    top.update({player[1][2]:[player[0], player[1][1], player[1][0]]})
            for player in top:
                print(f"{player}, {top[player][0]}, {top[player][1]}, {top[player][2]}")
            print()
        elif choice == 'f':
            top = {}
            for player in sorted_players:
                if player[1][2] not in list(top.keys()) and player[1][1] == 'F':
                    top.update({player[1][2]:[player[0], player[1][1], player[1][0]]})
            for player in top:
                print(f"{player}, {top[player][0]}, {top[player][1]}, {top[player][2]}")
            print()
        else:
            print("Incorrect input")
            continue
        while True:
            loop = input("(V)iew more stat or (B)ack to main menu: ").lower()
            if loop == 'v':
                break
            elif loop == 'b':
                return
            else:
                print("Incorrect input")
read_player()
while True:
    print('-------------')
    print('>>> Main menu\n1.Play game\n2.Add player’s budget\n3.View player’s profile\n4.View stat\n5.Quit program')
    action = input('Enter menu choice: ')
    if action == '1':
        print('-------------\nBlackjack starting…')
        play()
    elif action == '2':
        print("-------------")
        add_budget()
    elif action == '3':
        print("-------------")
        view_profile()
    elif action == '4':
        print("-------------")
        view_stat()
    elif action == '5':
        print("-------------\nBye!")
        break
    else:
        print("Invalid input")