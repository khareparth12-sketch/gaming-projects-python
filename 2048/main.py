import pygame
import random
import math
from .constants import *

def main():
    pygame.init()

    WIN = pygame.display.set_mode(WINDOW_SIZE[0], WINDOW_SIZE[1])
    pygame.display.set_caption("2048 Game")

if __name__ == "__main__":
    main()