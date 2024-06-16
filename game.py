import pygame
import elements
import time
from colors import Colors
pygame.init()

screen = pygame.display.set_mode([800, 800])

board = elements.Board(8)
board.map[5][5].alive = True
board.map[5][6].alive = True
board.map[5][7].alive = True


running = True

def draw():
    screen.fill((255, 255, 255))
    for y in range(board.cell_amount):
        for x in range(board.cell_amount):
            pygame.draw.rect(screen,Colors.gray,pygame.Rect(x*8,y*8,8,8),1)
            if board.map[x][y].alive == True:
                pygame.draw.rect(screen,Colors.black,pygame.Rect(x*8,y*8,8,8))

def update():
    nextStep = elements.Board(8)
    for y in range(1,board.cell_amount):
        for x in range(1,board.cell_amount):
            evolutionPoints = int((
                        board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y].getValue() + 
                        board.map[x+1 if x+1 < board.cell_amount else 0][y].getValue() +  
                        board.map[x][y-1 if y-1 >= 0 else board.cell_amount-1].getValue() + 
                        board.map[x][y+1 if y+1 < board.cell_amount else 0].getValue() + 
                        board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y-1 if y-1 >= 0 else board.cell_amount-1].getValue() + 
                        board.map[x+1 if x+1 <board.cell_amount else 0][y-1 if y-1 >= 0 else board.cell_amount-1].getValue() + 
                        board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y+1 if y+1 < board.cell_amount else 0].getValue() + 
                        board.map[x+1 if x+1 < board.cell_amount else 0][y+1 if y+1 < board.cell_amount else 0].getValue()
                        ))
            if board.map[y][x].alive == True: 
                if (evolutionPoints < 2) or (evolutionPoints > 3): 
                    nextStep.map[y][x].alive = False
            else: 
                if evolutionPoints == 3: 
                    nextStep.map[y][x].alive = True
                    pygame.draw.rect(screen,Colors.red,pygame.Rect(x*8,y*8,8,8))
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


def testValues():
    
    for y in range(1,board.cell_amount):
        for x in range(1,board.cell_amount):
            points = int((
                board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y].getValue() + 
                board.map[x+1 if x+1 < board.cell_amount else 0][y].getValue() +  
                board.map[x][y-1 if y-1 >= 0 else board.cell_amount-1].getValue() + 
                board.map[x][y+1 if y+1 < board.cell_amount else 0].getValue() + 
                board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y-1 if y-1 >= 0 else board.cell_amount-1].getValue() + 
                board.map[x+1 if x+1 <board.cell_amount else 0][y-1 if y-1 >= 0 else board.cell_amount-1].getValue() + 
                board.map[x-1 if x-1 >= 0 else board.cell_amount-1][y+1 if y+1 < board.cell_amount else 0].getValue() + 
                board.map[x+1 if x+1 < board.cell_amount else 0][y+1 if y+1 < board.cell_amount else 0].getValue()
                ))
            if points == 3: 
                pygame.draw.rect(screen,Colors.red,pygame.Rect(x*8,y*8,8,8))
            print(points)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    draw()
    #test()
    testValues()
    update()
    pygame.display.flip()
    time.sleep(2)

pygame.quit()

