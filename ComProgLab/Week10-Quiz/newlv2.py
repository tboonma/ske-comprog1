import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
print(team_list)

pos_label = ['MP', 'win', 'draw', 'lose', 'gf', 'ga', 'gd', 'pts']
all_team = dict()
for i in range(1, len(team_list)):
    team_in_dict = list(all_team.keys())
    if team_list[i][0] not in team_in_dict:
        all_team.update({team_list[i][0]:[0,0,0,0,0,0,0,0]})
    if team_list[i][1] not in team_in_dict:
        all_team.update({team_list[i][1]:[0,0,0,0,0,0,0,0]})
    temp_team1 = all_team[team_list[i][0]]
    temp_team2 = all_team[team_list[i][1]]
    temp_team1[0] += 1
    temp_team2[0] += 1
    if int(team_list[i][2]) > int(team_list[i][3]):
        temp_team1[1] += 1
        temp_team2[3] += 1
    elif int(team_list[i][2]) < int(team_list[i][3]):
        temp_team1[3] += 1
        temp_team2[1] += 1
    else:
        temp_team1[2] += 1
        temp_team2[2] += 1
    temp_team1[4] += int(team_list[i][2])
    temp_team2[4] += int(team_list[i][3])
    temp_team1[5] += int(team_list[i][3])
    temp_team2[5] += int(team_list[i][2])
    temp_team1[6] = temp_team1[4] - temp_team1[5]
    temp_team2[6] = temp_team2[4] - temp_team2[5]
    temp_team1[7] = temp_team1[1]*3 + temp_team1[2]
    temp_team2[7] = temp_team2[1]*3 + temp_team2[2]

listed_team = {x : y for x,y in sorted(all_team.items(), key=lambda item: (item[1][7],item[1][6],item[1][4]/item[1][0]), reverse=True)}


print(f"{'Club':^26} {'MP':>3}  W   D   L   GF  GA  GD  Pts")
order = 1
for team in listed_team:
    print(f"{str(order) + '.':<6} {team:<20} {listed_team[team][0]:<3} {listed_team[team][1]:<3} {listed_team[team][2]:<3} {listed_team[team][3]:<3} {listed_team[team][4]:<3} {listed_team[team][5]:<3} {listed_team[team][6]:<3} {listed_team[team][7]:<3}")
    order += 1