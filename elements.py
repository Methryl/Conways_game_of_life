class Cell:
    x = 0
    y = 0
    ALIVE = (0,0,0)
    DEAD = (255,255,255)
    states = [ALIVE,DEAD]
    state = DEAD
    size = 16


class Board:
    map = []
    def __init__(self, TILE_SIZE):
        cell_amount = int(800/TILE_SIZE)
        for y in range(cell_amount):
            row = []
            for x in range(cell_amount):
                cell = Cell()
                cell.x = x+TILE_SIZE
                cell.y = y+TILE_SIZE
                row.append(cell)
            self.map.append(row)