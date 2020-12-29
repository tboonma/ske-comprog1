import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
#print(team_list)

def score_table_lv1(team_list):
    teams_name_temp = []
    team_name = []
    team_total_matches = []
    team_win = {}
    team_lose = {}
    team_draw = {}
    for i in range(1,len(team_list)):
        teams_name_temp.append(team_list[i][0])
        teams_name_temp.append(team_list[i][1])
    for team in teams_name_temp:
        if team not in team_name:
            team_name.append(team)
            team_total_matches.append(teams_name_temp.count(team))
    for i in range(1,len(team_list)):
        if int(team_list[i][2]) > int(team_list[i][3]):
            try:
                temp = team_win[team_list[i][0]] + 1
                team_win.update({team_list[i][0]:temp})
            except:
                team_win.update({team_list[i][0]:1})
            try:
                temp = team_lose[team_list[i][1]] + 1
                team_lose.update({team_list[i][1]:temp})
            except:
                team_lose.update({team_list[i][1]:1})
        elif int(team_list[i][2]) < int(team_list[i][3]):
            try:
                temp = team_win[team_list[i][1]] + 1
                team_win.update({team_list[i][1]:temp})
            except:
                team_win.update({team_list[i][1]:1})
            try:
                temp = team_lose[team_list[i][0]] + 1
                team_lose.update({team_list[i][0]:temp})
            except:
                team_lose.update({team_list[i][0]:1})
        else:
            try:
                temp = team_draw[team_list[i][0]] + 1
                team_draw.update({team_list[i][0]:temp})
            except:
                team_draw.update({team_list[i][0]:1})
            try:
                temp = team_draw[team_list[i][1]] + 1
                team_draw.update({team_list[i][1]:temp})
            except:
                team_draw.update({team_list[i][1]:1})
    print(f"{'Club':^26} {'MP':>3}  W D L")
    for i in range(len(team_name)):
        try:
            win = team_win[team_name[i]]
        except:
            win = 0
        try:
            lose = team_lose[team_name[i]]
        except:
            lose = 0
        try:
            draw = team_draw[team_name[i]]
        except:
            draw = 0
        print(f"{i+1:<6} {team_name[i]:<20} {team_total_matches[i]:<3} {win} {draw} {lose}")

score_table_lv1(team_list)