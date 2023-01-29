# Imports
import pygame
import sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()
level = Level(level_map, screen)
pygame.display.set_caption("Dawn of Malevolence")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # set background color to our window
    screen.blit(background, (0, 0))
    level.run()

    # Update our window
    pygame.display.update()
    clock.tick(60)

#VIDEO: https://www.youtube.com/watch?v=YWN8GcmJ-jA#
