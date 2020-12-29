import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
# print(team_list)

pos_label = ['MP', 'win', 'draw', 'lose']
all_team = dict()
for i in range(1, len(team_list)):
    team_in_dict = list(all_team.keys())
    if team_list[i][0] not in team_in_dict:
        all_team.update({team_list[i][0]:[0,0,0,0]})
    if team_list[i][1] not in team_in_dict:
        all_team.update({team_list[i][1]:[0,0,0,0]})
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
print(f"{'Club':^26} {'MP':>3}  W D L")
order = 1
for team in all_team:
    print(f"{order:<6} {team:<20} {all_team[team][0]:<3} {all_team[team][1]} {all_team[team][2]} {all_team[team][3]}")
    order += 1