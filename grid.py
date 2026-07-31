from cells import Cell
class Grid():
    def __init__(self, size_x:int, size_y:int):
        self.size_x = size_x
        self.size_y = size_y
        self.list_of_cells = [[Cell() for _ in range(size_y)] Cell() for _ in range(size_x)] #creates a 2D array full of 0s that represent a grid of dead cells 

    def add_cell(self, cell_position: tuple(x:int, y:int)):
        self.list_of_cells[cell_position[0]][cell_position[1]].alive = True 
        for i in range(-1, 1):
            for j in range(-1, 1):
                self.list_of_cells[cell_position[0] + i][cell_position[1] + j].neighbours += 1

    def delete_cell(self, cell_position: tuple(x:int, y:int)):
        self.list_of_cells[cell_position[0]][cell_position[1]].alive = False
        for i in range(-1, 1):
            for j in range(-1, 1):
                self.list_of_cells[cell_position[0] + i][cell_position[1] + j].neighbours -= 1

    def check_neighbour_cells(self):
        cells_to_delete = []
        cells_to_add = []
        for x in self.list_of_cells:
            for y in self.list_of_cells:
                cell = self.list_of_cells[x][y]
                if cell.neighbours == 2 or 3 and cell.alive:
                    continue
                elif cell.neighbours > 3 and cell.alive:
                    cells_to_delete.append((x, y))
                elif cell.neighbours == 3 and not cell.alive:
                    cells_to_add.append((x, y))

        for cell in cells_to_add:
            add_cell(cell)
        for cell in cells_to_delete:
            delete_cell(cell)


