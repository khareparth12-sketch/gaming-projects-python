import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer Game")

BACKGROUND = (144, 201, 120)
WIDTH, HEIGHT = 900, 700
FPS = 60
PLAYER_VEL = 5
# GRAVITY = 1
# JUMP_VEL = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main(screen):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()      

if __name__ == "__main__":
    main(screen)