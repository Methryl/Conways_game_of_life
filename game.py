import pygame
import elements
pygame.init()

screen = pygame.display.set_mode([800, 800])

board = elements.Board(8)
print(board.map[3][3].state)
running = True
while running:

    # Handle exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background with white
    screen.fill((255, 255, 255))
    for y in range(200):
        for x in range(200):
            pygame.draw.rect(screen,(255,255,255),pygame.Rect(x*8,y*8,6,6),0)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()