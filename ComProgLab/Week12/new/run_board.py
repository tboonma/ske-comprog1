from board import *
from player import *
from cell import *
import random

select_board = 'board' + str(random.randint(1,3)) + '.txt'
board = Board(select_board)

all_player = []
num = int(input('Input total player : '))
for i in range(num):
    name = chr(65+i)
    all_player.append(Player(name))
order_player = []
while True:
    rand_player = random.randint(0,num-1)
    if all_player[rand_player] not in order_player:
        order_player.append(all_player[rand_player])
        board.add_player(all_player[rand_player]) 
    if len(order_player) == len(all_player):
        break

print('Starting...')
print(board)

round = 1
win = False
while True:
    print(">>> Round {}".format(round))
    round += 1
    for player in order_player:
        player.randomize_dice()
        if player.current_hold == 'TRUE':
            print('{} holds.'.format(player.name))
        else:
            print(player.name + '\'s position = ' + str(player.current_pos) + '. ',end='') 
            print(player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        if board.check_winner():
            win = True
            break
    if win:
        print(f"Game over. {board.get_winner().name} wins!")
        break
