from cells import Cell
class Grid():
    def __init__(self, size_x:int, size_y:int):
        self.size_x = size_x
        self.size_y = size_y
        self.grid_of_cells = [[Cell() for _ in range(size_y)] for _ in range(size_x)] #creates a 2D array full of 0s that represent a grid of dead cells 

    def __repr__(self):
        return f"{self.grid_of_cells}"    

    def __eq__(self, other):
        if isinstance(other, Grid):
            if self.grid_of_cells == other.grid_of_cells:
                return True
            else:
                return False
        elif isinstance(other, list):
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.grid_of_cells[i][j] == other[i][j]:
                        continue
                    else:
                        return False
            return True
        elif f"{self}" == other:
            return True
        return False

    def __getitem__(self, index: tuple[int, int]) -> Cell:
        return self.grid_of_cells[index[0]][index[1]]

    def add_cell(self, cell_position: tuple[int, int]):
        self[cell_position].alive = True 
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                #this will run into an out of index issue, fix
                self.grid_of_cells[cell_position[0] + i][cell_position[1] + j].neighbours += 1

    def delete_cell(self, cell_position: tuple[int, int]):
        self[cell_position].alive = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                #same here
                if self.grid_of_cells[cell_position[0] + i][cell_position[1] + j].neighbours >= 1:
                    self.grid_of_cells[cell_position[0] + i][cell_position[1] + j].neighbours -= 1

    def check_neighbour_cells(self):
        cells_to_delete = []
        cells_to_add = []
        for i in range(self.size_x):
            for j in range(self.size_y):
                cell = self.grid_of_cells[i][j]
                if cell.alive and cell.neighbours == 2 or cell.alive and cell.neighbours == 3:
                    continue
                elif cell.alive and cell.neighbours > 3 or cell.alive and cell.neighbours <= 1:
                    cells_to_delete.append((i, j))
                elif not cell.alive and cell.neighbours == 3:
                    cells_to_add.append((i, j))

        for cell in cells_to_add:
            add_cell(cell)
        for cell in cells_to_delete:
            delete_cell(cell)


