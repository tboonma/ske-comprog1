import urllib.request
import csv
import codecs
csv_url = "http://eduserv.ku.ac.th/EPL2020.csv"

class Football:
    def __init__(self, short_name='', full_name='', win=0, draw=0, lose=0):
        self.__full_name = full_name
        self.__short_name = short_name
        self.__win = int(win)
        self.__draw = int(draw)
        self.__lose = int(lose)

    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, name):
        self.__full_name = name
    
    @property
    def short_name(self):
        return self.__short_name
    
    @short_name.setter
    def short_name(self, name):
        self.__short_name = name
    
    @property
    def win(self):
        return self.__win
    
    @win.setter
    def win(self, new_win):
        self.__win = new_win
    
    @property
    def draw(self):
        return self.__draw
    
    @draw.setter
    def draw(self, new_draw):
        self.__draw = new_draw
    
    @property
    def lose(self):
        return self.__lose
    
    @lose.setter
    def lose(self, new_lose):
        self.__lose = new_lose
    
    def won(self, other):
        self.__win += 1
        other.__lose += 1
    
    def drew(self, other):
        self.__draw += 1
        other.__draw += 1

    def losed(self, other):
        self.__lose += 1
        other.__win += 1

    def __str__(self):
        return f"{self.__full_name},{self.__short_name},{self.__win},{self.__draw},{self.__lose}"

class FileReadFromURL:
    def __init__(self):
        self.data = []
    
    def read(self, url):
        file = urllib.request.urlopen(url)
        rows = csv.DictReader(codecs.iterdecode(file, 'utf-8'))
        for team in rows:
            self.data.append(Football(team['Short Name'], team['Full Name'], team['Win'], team['Draw'], team['Loss']))
    
    def print_list_team(self):
        for team in self.data:
            print(f"{team.short_name},{team.full_name},{team.win},{team.draw},{team.lose}")