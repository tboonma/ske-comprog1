from football import *

a = FileReadFromURL()
a.read(csv_url)
while True:
    action = input("(s)how summary (e)nter results (q)uit: ").lower()
    if action == 'q':
        print("Bye")
        break
    if action == 's':
        a.print_list_team()
    elif action == 'e':
        result = input("Enter a result: ")
        compute = result.split()
        for team in a.data:
            if team.short_name == compute[0]:
                team1 = team
            elif team.short_name == compute[2]:
                team2 = team
        if compute[1] == 'won':
            team1.won(team2)
        elif compute[1] == 'losed':
            team1.losed(team2)
        elif compute[1] == 'drew':
            team1.drew(team2)
        else:
            print("Error")