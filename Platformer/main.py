import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer Game")

WIDTH, HEIGHT = 900, 700
FPS = 60
PLAYER_VEL = 5
# GRAVITY = 1
# JUMP_VEL = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        self.direction = "left"
        self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        self.direction = "right"
        self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)
        
def get_bg(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, w, h = image.get_rect()
    tiles = []

    for i in range(WIDTH//w +1):
        for j in range(HEIGHT//h +1):
            pos = (i*w, j*h)
            tiles.append(pos)

    return tiles, image

def draw(screen, bg, bg_img, player):
    for tile in bg:
        screen.blit(bg_img, tile)

    player.draw(screen)

    pygame.display.update()

def main(screen):
    clock = pygame.time.Clock()
    bg, bg_img = get_bg("Brown.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(screen, bg, bg_img, player)

    pygame.quit()
    quit()      

if __name__ == "__main__":
    main(screen)