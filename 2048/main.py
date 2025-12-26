import pygame
import random
import math

pygame.init()

FPS = 60
HIEGHT, WIDTH = 700, 700
ROW = 4
COL = 4

CELL_HEIGHT = HIEGHT // ROW
CELL_WIDTH = WIDTH // COL

BORDER_COLOR = (187, 173, 160)
BORDER = 10
BACKGROUND_COLOR = (250, 248, 239)
FONT_COLOR = (119, 110, 101)

MOVE_VEL = 20
FONT = pygame.font.SysFont("comicsans", 50, bold=True)

WIN = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("2048 Game")

def main(WIN):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == "__main__":
    main(WIN)