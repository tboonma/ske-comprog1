def order_maxtomin(teams_winrate,winrate_list):
    winrate_list.sort(reverse = True)
    for i in winrate_list:
        print(f"{teams_winrate[i]}: got win rate {i:.5f}")

def order_mintomax(teams_winrate,winrate_list):
    winrate_list.sort()
    for i in winrate_list:
        print(f"{teams_winrate[i]}: got win rate {i:.5f}")

file_name = input("Enter a file name: ")
f = open(file_name, "r")
teams_winrate = dict()
winrate_list = []
for i in f:
    text_type = 1
    team_name = ""
    win = ""
    lose = ""
    for j in i:
        if j == ',':
            text_type += 1
        else:
            if text_type == 1:
                team_name += j
            elif text_type == 2:
                win += j
            elif text_type == 3:
                lose += j
    win = int(win)
    lose = int(lose)
    winrate = win/(win+lose)
    teams_winrate.update({winrate : team_name})
    winrate_list.append(winrate)
winrate_list.sort()
total = len(winrate_list)

while True:
    action = input("What do you want to know ? (m)in , ma(x), (o)rder max to min, o(r)der min to max, (q)uit : ").lower()
    if action == 'o':
        print(f"\nTotal team(s): {total}")
        order_maxtomin(teams_winrate,winrate_list)
        print()
    elif action == 'r':
        print(f"\nTotal team(s): {total}")
        order_mintomax(teams_winrate,winrate_list)
        print()
    elif action == 'm':
        print(f"\n{teams_winrate[winrate_list[0]]} got minimum win rate {winrate_list[0]:.5f}\n")
    elif action == 'x':
        print(f"\n{teams_winrate[winrate_list[len(winrate_list)-1]]} got maximum win rate {winrate_list[len(winrate_list)-1]:.5f}\n")
    elif action == 'q':
        print("Bye")
        break

f.close()