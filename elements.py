
class Cell:
    
    def __init__(self,x,y,alive=False):
        self.x = x
        self.y = y
        self.alive = alive
        self.nextState = None
        self.size = 16

    def neighbors(self):
        yield (self.x+1, self.y)
        yield (self.x-1, self.y)
        yield (self.x, self.y+1)
        yield (self.x, self.y-1)
        yield (self.x+1, self.y+1)
        yield (self.x-1, self.y-1)
        yield (self.x-1, self.y+1)
        yield (self.x+1, self.y-1)


class Board:
    def __init__(self, TILE_SIZE):
        self.cells = {}
        self.cell_amount = int(800/TILE_SIZE)
        for y in range(self.cell_amount):
            for x in range(self.cell_amount):
                self.cells[x,y] = Cell(x,y)