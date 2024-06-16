import pygame
import elements
import time
import math
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
        if board.cells[x,y].alive == True and (aliveNeighbors < 2) or (aliveNeighbors > 3):
            nextStep.cells[x,y].alive = False
        elif board.cells[x,y].alive == True and 2<=aliveNeighbors<=3 or board.cells[x,y].alive == False and aliveNeighbors == 3:
            nextStep.cells[x,y].alive = True
    return nextStep

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

    paused = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = (math.floor(pygame.mouse.get_pos()[0]/8),math.floor(pygame.mouse.get_pos()[1]/8))
                board.cells[pos].alive = True
                pygame.draw.rect(screen,Colors.black,pygame.Rect(pos[0]*8,pos[1]*8,8,8))
        if not paused:
            board = update(board)
            time.sleep(0.1)
        else:
            pass
        draw(board)
        pygame.display.flip()

if __name__ == "__main__":
    main()

