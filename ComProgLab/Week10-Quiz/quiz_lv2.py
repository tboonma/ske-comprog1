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

def score_table_lv2(team_list):
    teams_name_temp = []
    team_name = []
    team_total_matches = []
    team_win = {}
    team_lose = {}
    team_draw = {}
    team_gf = {}
    team_ga = {}
    team_pts = {}
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
            try:
                temp = team_pts[team_list[i][0]] + 3
                team_pts.update({team_list[i][0]:temp})
            except:
                team_pts.update({team_list[i][0]:3})
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
            try:
                temp = team_pts[team_list[i][1]] + 3
                team_pts.update({team_list[i][1]:temp})
            except:
                team_pts.update({team_list[i][1]:3})
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
            try:
                temp = team_pts[team_list[i][0]] + 1
                team_pts.update({team_list[i][0]:temp})
            except:
                team_pts.update({team_list[i][0]:1})
            try:
                temp = team_pts[team_list[i][1]] + 1
                team_pts.update({team_list[i][1]:temp})
            except:
                team_pts.update({team_list[i][1]:1})
        try:
            temp = team_gf[team_list[i][0]] + int(team_list[i][2])
            team_gf.update({team_list[i][0]:temp})
        except:
            team_gf.update({team_list[i][0]:int(team_list[i][2])})
        try:
            temp = team_ga[team_list[i][0]] + int(team_list[i][3])
            team_ga.update({team_list[i][0]:temp})
        except:
            team_ga.update({team_list[i][0]:int(team_list[i][3])})
        try:
            temp = team_gf[team_list[i][1]] + int(team_list[i][3])
            team_gf.update({team_list[i][1]:temp})
        except:
            team_gf.update({team_list[i][1]:int(team_list[i][3])})
        try:
            temp = team_ga[team_list[i][1]] + int(team_list[i][2])
            team_ga.update({team_list[i][1]:temp})
        except:
            team_ga.update({team_list[i][1]:int(team_list[i][2])})
    team_gd = []
    for team in team_name:
        temp = team_gf[team]-team_ga[team]
        team_gd.append(temp)
    print(f"{'Club':^26} {'MP':>3}  W   D   L   {'GF':<3} {'GA':<3} {'GD':<3} {'Pts':<3}")
    all_team_pts = list(team_pts.keys())
    zero = len(team_name) - len(all_team_pts)
    all_pts = list(team_pts.values()) + [0]*zero
    all_pts.sort(reverse=True)
    # for i in range(len(team_name)):
    #     try:
    #         win = team_win[team_name[i]]
    #     except:
    #         win = 0
    #     try:
    #         lose = team_lose[team_name[i]]
    #     except:
    #         lose = 0
    #     try:
    #         draw = team_draw[team_name[i]]
    #     except:
    #         draw = 0
    #     try:
    #         pts = team_pts[team_name[i]]
    #     except:
    #         pts = 0
    #     print(f"{i+1:<6} {team_name[i]:<20} {team_total_matches[i]:<3} {win:<3} {draw:<3} {lose:<3} {team_gf[team_name[i]]:<3} {team_ga[team_name[i]]:<3} {team_gd[i]:<3} {pts:<3}")
    all_team = []
    for i in range(len(team_name)):
        temp = dict()
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
        try:
            pts = team_pts[team_name[i]]
        except:
            pts = 0
        temp.update({'name':team_name[i]})
        temp.update({'total':int(team_total_matches[i])})
        temp.update({'win':int(win)})
        temp.update({'draw':int(draw)})
        temp.update({'lose':int(lose)})
        temp.update({'gf':int(team_gf[team_name[i]])})
        temp.update({'ga':int(team_ga[team_name[i]])})
        temp.update({'gd':int(team_gd[i])})
        temp.update({'pts':int(pts)})
        all_team.append(temp)
    pts_counted = []
    pts_order = []
    for i in all_pts:
        if i in pts_counted:
            continue
        if all_pts.count(i) > 1:
            temp_gd = []
            for team in all_team:
                if team['pts'] == i:
                    temp_gd.append(team['gd'])
                temp_gd.sort(reverse=True)
            pts_order.extend(temp_gd)
        pts_counted.append(i)
    order = 1
    for i in all_pts:
        if all_pts.count(i) > 1:
            gd = pts_order[0]
            pts = i
            for i in all_team:
                if i['pts'] == pts and i['gd'] == gd:
                    name = i['name']
                    total = i['total']
                    win = i['win']
                    lose = i['lose']
                    draw = i['draw']
                    gf = i['gf']
                    ga = i['ga'] 
            pts_order.pop(0)
        else:
            pts = i
            for i in all_team:
                if i['pts'] == pts:
                    gd = team['gd']
                    name = i['name']
                    total = i['total']
                    win = i['win']
                    lose = i['lose']
                    draw = i['draw']
                    gf = i['gf']
                    ga = i['ga']
        print(f"{name:<20} {total:<3} {win:<3} {draw:<3} {lose:<3} {gf:<3} {ga:<3} {gd:<3} {pts:<3}")
score_table_lv2(team_list)