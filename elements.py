
class Cell:
    x = 0
    y = 0
    alive = False
    size = 16


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