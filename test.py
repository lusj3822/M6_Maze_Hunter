import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Hunter")
clock = pygame.time.Clock() # Framerate

test_surface = pygame.Surface((100,200))
test_surface.fill("RED")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (250,250))

    pygame.display.update()
    
    clock.tick(60) # Framerate


    
