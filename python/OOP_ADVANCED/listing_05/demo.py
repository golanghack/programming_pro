import pygame
from pygame.locals import * 
import sys 

BLACK = (100, 10, 0)
WIDTH = 960
HEIGHT = 540
FRAME_SECONDS = 22

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    window.fill(BLACK)
    pygame.display.update()

    clock.tick(FRAME_SECONDS)
