import pygame
import elements
import time
from colors import Colors
pygame.init()

screen = pygame.display.set_mode([800, 800])



def draw(board):
    screen.fill((255, 255, 255))
    for (x,y) in board.cells:
        pygame.draw.rect(screen,Colors.gray,pygame.Rect(x*8,y*8,8,8),1)
        if board.cells[x,y].alive == True:
            pygame.draw.rect(screen,Colors.black,pygame.Rect(x*8,y*8,8,8))

def update(board):
    nextStep = elements.Board(8)
    for (x,y) in board.cells:
        aliveNeighbors = 0
        for cell in board.cells[x,y].neighbors():
            try:
                if board.cells[cell].alive:
                    aliveNeighbors+=1
            except Exception as e:
                pass
        if aliveNeighbors > 0:
            print(aliveNeighbors)
        if board.cells[x,y].alive == True and (aliveNeighbors < 2) or (aliveNeighbors > 3):
            nextStep.cells[x,y].alive = False
        elif board.cells[x,y].alive == True and 2<=aliveNeighbors<=3 or board.cells[x,y].alive == False and aliveNeighbors == 3:
            nextStep.cells[x,y].alive = True
    return nextStep
    
def test():
    x = 50
    y = 6
    board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y].alive = True
    board.map[x+1 if x+1 < board.cell_amount else 0][y].alive = True 
    board.map[x][y-1 if y-1 >= 0 else board.cell_amount-1].alive = True
    board.map[x][y+1 if y+1 < board.cell_amount else 0].alive = True
    board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y-1 if y-1 >= 0 else board.cell_amount-1].alive = True
    board.map[x+1 if x+1 <board.cell_amount else 0][y-1 if y-1 >= 0 else board.cell_amount-1].alive = True 
    board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y+1 if y+1 < board.cell_amount else 0].alive = True 
    board.map[x+1 if x+1 < board.cell_amount else 0][y+1 if y+1 < board.cell_amount else 0].alive = True


def main():
    board = elements.Board(8)


    board.cells[5,5].alive = True
    board.cells[5,6].alive = True
    board.cells[5,7].alive = True

    board.cells[10,10].alive = True
    board.cells[10,12].alive = True
    board.cells[9,12].alive = True
    board.cells[11,12].alive = True
    board.cells[11,11].alive = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        
        draw(board)
        board = update(board)
        pygame.display.flip()
        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()

