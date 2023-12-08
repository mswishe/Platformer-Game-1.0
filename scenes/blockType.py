import pygame
import os
from os.path import join

def get_terrain_block(size, x, y):
    path = join("assets", "Terrain", "Terrain (16x16).png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(x, y, size, size)
    surface.blit(image, (0,0), rect)
    return pygame.transform.scale2x(surface)


def get_block(size, type):
    match type:
        case 'greenGrass':
            return get_terrain_block(size, 96, 0)
        case _:
            return
         
        