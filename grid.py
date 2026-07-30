from cells import Cell
class Grid():
    def __init__(self, size_x:int, size_y:int, list_of_cells:list):
        self.size_x = size_x
        self.size_y = size_y
        self.list_of_cells = list_of_cells

    def add_cell(self, pos_x, pos_y):
        self.list_of_cells.append(Cell(pos_x, pos_y, True))
        self.sort_cells()

    def sort_cells(self):
        #implement sorting algorithm for cells



