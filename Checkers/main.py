import pygame
from checkers.constant import WIDTH, HEIGHT, CELL, YELLOW
from checkers.game import Game
#from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

def get_input_from_mouse(pos):
    x, y = pos
    row = y // CELL
    col = x // CELL
    return row, col

def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while running:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_input_from_mouse(pos)
                game.select_piece(row, col)
        
        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()