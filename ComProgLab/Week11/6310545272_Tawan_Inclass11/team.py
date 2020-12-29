import random
from player import *

class Team:
    def __init__(self, filename, team_name='No Name', team_points=0, current_player=0): 
        self.__player_list = self.__read_team(filename)
        self.__team_name = team_name
        self.__team_points = team_points
        self.__current_player = current_player
        self.current_player = []
    
    def __read_team(self, filename):
        player_list = []
        with open(filename, 'r') as f:
            rows = f.readlines()
            for i in rows:
                player_list.append(i.strip().split(', '))
        for player in player_list:
            player[1] = int(player[1])
            player[2] = int(player[2])
            player.append('None')
        print(player_list)
        return player_list

    def select_player(self):
        self.current_player = ""
        rand_player = random.randint(0,len(self.__player_list)-1)
        hand_num = random.randint(1,3)
        if hand_num == 1:
            self.__player_list[rand_player][3] = 'Rock'
        elif hand_num == 2:
            self.__player_list[rand_player][3] = 'Paper'
        elif hand_num == 3:
            self.__player_list[rand_player][3] = 'Scissors'
        else:
            self.__player_list[rand_player][3] = 'Error {0}'.format(hand_num)
        self.__player = self.__player_list[rand_player]
        self.current_player += "{0}: Wins = {1}: Plays = {2}: Hand = {3}".format(self.__player[0], self.__player[1], self.__player[2], self.__player[3])

    def update_team_points(self, value):
        if value.lower() == 'win':
            self.__team_points += 1
            self.__player[1] += 1
            self.__player[2] += 1
        elif value.lower() == 'lose':
            self.__player[2] += 1

    def __str__(self):
        output = "Team {0}\n".format(self.__team_name)
        output += "Team Points: {0}\n".format(self.__team_points)
        for player in self.__player_list:
            output += "{0}: Wins = {1}: Plays = {2}: Hand = {3}\n".format(player[0], player[1], player[2], player[3])
        return output
