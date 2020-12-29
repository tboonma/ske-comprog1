from cell import Cell

class Board:
    def __init__(self, filename):
        self.__cell_list = []
        self.__length = 0
        self.__width = 0
        self.__read_board(filename)

    def __read_board(self, filename):
        f = open(filename, 'r')
        rows = f.read().splitlines()
        self.__width = int(rows[0])
        self.__length = int(rows[1])
        for i in range(2, len(rows)):
            txt = rows[i].split(',')
            self.__cell_list.append(Cell(txt[0], txt[1], txt[2]))
    
    @property
    def cell_list(self):
        return self.__cell_list
    
    def add_player(self, player):
        first_cell = self.__cell_list[0]
        first_cell.add_occupy_list(player)

    def access_cell(self, id):
        selected_cell = self.__cell_list[id]
        return selected_cell

    def check_winner(self):
        last = len(self.__cell_list) - 1
        if self.__cell_list[last].get_occupy_list_str() != "":
            return True
        else:
            return False
    
    def get_winner(self):
        last = len(self.__cell_list) - 1
        if self.check_winner():
            return self.__cell_list[last].occupy_list[0]

    def update_board(self, player):
        if player.current_hold == 'TRUE':
            player.current_hold = 'FALSE'
            return
        while True:
            new_pos = player.current_pos + player.current_move
            if new_pos > len(self.__cell_list) - 1:
                new_pos = len(self.__cell_list) - 1
            self.__cell_list[new_pos].add_occupy_list(player)
            self.__cell_list[player.current_pos].remove_occupy_list(player)
            player.move(self)
            player.obtain_cell_status(self)
            if int(player.current_move) == 0:
                break
    
    def __str__(self):
        col = self.__width
        output = "-" * col*8 + "-"
        for i in range(self.__length):
            start = i*self.__width
            stop = i*self.__width+self.__width
            step = 1
            if i % 2 == 1:
                start = i*self.__width+self.__width - 1
                stop = i*self.__width - 1
                step = -1
            output += "\n|"
            for j in range(start, stop, step):
                output += "{:^7}|".format(j)
            output += "\n|"
            for j in range(start, stop, step):
                cell_detail = self.__cell_list[j].move + "," + self.__cell_list[j].hold[0]
                output += "{:^7}|".format(cell_detail)
            output += "\n|"
            for j in range(start, stop, step):
                detail = self.__cell_list[j].get_occupy_list_str()
                output += "{:^7}|".format(detail)
            output += "\n"
            output += "-" * col*8 + "-"
        return output+"\n"

