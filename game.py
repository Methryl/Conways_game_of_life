import pygame
import elements
import time
from colors import Colors
pygame.init()

screen = pygame.display.set_mode([800, 800])

board = elements.Board(8)
board.map[3][3].alive=True
running = True

def draw():
    screen.fill((255, 255, 255))
    for y in range(board.cell_amount):
        for x in range(board.cell_amount):
            pygame.draw.rect(screen,Colors.gray,pygame.Rect(x*8,y*8,8,8),1)
            if board.map[x][y].alive == True:
                pygame.draw.rect(screen,Colors.black,pygame.Rect(x*8,y*8,8,8))
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw()
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()

