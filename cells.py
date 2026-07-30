#a live cell with two or three live neighbors lives on, a live cell with more than three live neighbors dies (overpopulation), and a dead cell with exactly three live neighbors becomes alive (reproduction).
class Cell():
    def __init__(self, pos_x:int, pos_y:int, alive:bool):
        self.x = x
        self.y = y
        self.alive = alive
        self.neighbours = 0

    def __repr__(self):
        return f"pos x: {self.x}, pos y: {self.y}, alive {self.alive}"
    
    def check_neighbours(self):
        #if neighbours > 3 die
        #if neighbours == 2 or 3 live
        #if !self.alive and neighbours == 3 self.alive = true
    
