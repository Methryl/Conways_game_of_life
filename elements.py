
class Cell:
    x = 0
    y = 0
    alive = False
    value = 0
    size = 16
    def getValue(self):
        if self.alive == True:
            self.value = 1
        else:
            self.value = 0
        return int(self.value)


class Board:
    map = []
    cell_amount = 0
    def __init__(self, TILE_SIZE):
        self.cell_amount = int(800/TILE_SIZE)
        for y in range(self.cell_amount):
            row = []
            for x in range(self.cell_amount):
                cell = Cell()
                cell.x = x+TILE_SIZE
                cell.y = y+TILE_SIZE
                row.append(cell)
            self.map.append(row)