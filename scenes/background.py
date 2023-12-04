import pygame
import os
from os.path import join
import global_variables as gv

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(gv.WIDTH // width + 1):
        for j in range(gv.HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image