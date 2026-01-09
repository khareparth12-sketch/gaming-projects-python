import pygame
import random
import math

pygame.init() # Initializes the features we are gonna need

FPS = 60
HEIGHT, WIDTH = 700, 700
ROW = 4
COL = 4

CELL_HEIGHT = HEIGHT // ROW
CELL_WIDTH = WIDTH // COL

BORDER_COLOR = (187, 173, 160)
BORDER = 10
BACKGROUND_COLOR = (250, 248, 239)
FONT_COLOR = (119, 110, 101)

MOVE_VEL = 20
FONT = pygame.font.SysFont("comicsans", 50, bold=True)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to 2048 Game")

class Tiles:
    COLORS = [
        (237, 229, 218),
        (238, 224, 200),
        (242, 177, 121),
        (245, 149, 99),
        (246, 124, 95),
        (246, 94, 59),
        (237, 207, 114),
        (237, 204, 97),
        (237, 200, 80),
        (237, 197, 63),
        (237, 194, 46)
    ]

def draw_grid(WIN):
    for row in range(1, ROW):
        y = row * CELL_HEIGHT
        pygame.draw.line(WIN, BORDER_COLOR, (0, y), (WIDTH, y), BORDER)

    for col in range(1, COL):
        x = col * CELL_WIDTH
        pygame.draw.line(WIN, BORDER_COLOR, (x, 0), (x, HEIGHT), BORDER)

    pygame.draw.rect(WIN, BORDER_COLOR, (0, 0, WIDTH, HEIGHT), BORDER)

def draw(WIN):
    WIN.fill(BACKGROUND_COLOR)
    draw_grid(WIN)
    pygame.display.update()

def main(WIN):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS) # Loop runs only once every 60 seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(WIN)

    pygame.quit()

if __name__ == "__main__":
    main(WIN)