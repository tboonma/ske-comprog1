from cell import Cell
class Board:
    def __init__(self, filename):
        self.__cell_list = []
        self.__width = 0
        self.__length = 0
        self.read_board(filename)

    def read_board(self, filename):
        cell_list = []
        rows = open(filename).read().splitlines()
        for i in rows:
            temp = i.split(",")
            cell_list.append(temp)
        for i in cell_list:
            if len(i) > 1:
                self.__cell_list.append(Cell(i[0],i[1],i[2].title()))
        self.__width = cell_list[0][0]
        self.__length = cell_list[1][0]

    @property
    def cell_list(self):
        return self.__cell_list

    def add_player(self, player):
        first_cell = self.__cell_list[0]
        first_cell.add_occupy_list(player)
    
    def access_cell(self, cell_id):
        selected_cell = self.__cell_list[cell_id]
        return selected_cell

    def __str__(self):
        output = ""
        for i in self.__cell_list:
            output += str(i) + "\n"
        return output
