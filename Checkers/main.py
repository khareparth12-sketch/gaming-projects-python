import pygame
import time
import random
from checkers.constant import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def main():
    running = True
    clock = pygame.time.Clock()
    board = Board()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()