#a live cell with two or three live neighbors lives on, a live cell with more than three live neighbors dies (overpopulation), and a dead cell with exactly three live neighbors becomes alive (reproduction).
class Cell():
    def __init__(self, alive = False):
        self.neighbours = 0
        self.alive = alive 

    def __repr__(self):
        return f"alive {self.alive}, neighbours {self.neighbours}"

    def __eq__(self, other):
        if isinstance(other, Cell):
            if self.alive == other.alive and self.neighbours == other.neighbours:
                return True
            else:
                return False
        else:
            if f"{self}" == other:
                return True
            else:
                return False


    
    
