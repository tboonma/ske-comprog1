def find_winner(first_player, second_player):
    if first_player.find('Paper') != -1 and second_player.find('Rock') != -1:
        return 1
    elif first_player.find('Rock') != -1 and second_player.find('Scissors') != -1:
        return 1
    elif first_player.find('Scissors') != -1 and second_player.find('Paper') != -1:
        return 1
    elif second_player.find('Paper') != -1 and first_player.find('Rock') != -1:
        return 2
    elif second_player.find('Rock') != -1 and first_player.find('Scissors') != -1:
        return 2
    elif second_player.find('Scissors') != -1 and first_player.find('Paper') != -1:
        return 2
    else:
        return 0

def update_points(winning_team, first_team, second_team):
    if winning_team == 1:
        team_a.update_team_points('win')
        team_b.update_team_points('lose')
        print('A wins.')
    elif winning_team == 2:
        team_b.update_team_points('win')
        team_a.update_team_points('lose')
        print('B wins.')
    else:
        team_a.update_team_points('lose')
        team_b.update_team_points('lose')
        print('Both team tie.')

from team import *

# team_a = Team('team_a.txt','A') 
# print(team_a)
# team_b = Team('team_b.txt','B') 
# print(team_b)

# # 9
# team_a.select_player() 
# print(team_a.current_player)
# team_b.select_player() 
# print(team_b.current_player)

# # 10
# winning_team = find_winner(team_a.current_player, team_b.current_player)
# print(winning_team)

# # 11
# # team_a.update_team_points('win') 
# # print(team_a) 
# # team_b.update_team_points('lose') 
# # print(team_b)

# # 12
# update_points(winning_team, team_a, team_b) 
# print(team_a)
# print(team_b)

# 13
team_a = Team('team_a.txt','A') 
print(team_a)
team_b = Team('team_b.txt','B') 
print(team_b)

print("\n---------Start---------\n")

a_point = 0
b_point = 0
while a_point < 5 and b_point < 5:
    team_a.select_player() 
    print(team_a.current_player)
    team_b.select_player() 
    print(team_b.current_player)
    print()
    winning_team = find_winner(team_a.current_player, team_b.current_player)
    if winning_team == 1:
        a_point += 1
    elif winning_team == 2:
        b_point += 1
    update_points(winning_team, team_a, team_b) 
    print(team_a)
    print(team_b)
    print("-----------------------\n")
if a_point == 5:
    print('A wins.\n')
elif b_point == 5:
    print('B wins.\n')
