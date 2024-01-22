import pygame
import os
from os.path import join

def get_end_item(width, height):
    path = join("assets", "Items", "Checkpoints", "End", "End (Idle).png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, width, height)
    surface.blit(image, (0,0), rect)
    return pygame.transform.scale(surface, (width + width * 0.87, height + height * 0.87))

def get_item(width, height, type):
    match type:
        case 'end':
            return get_end_item(width, height)
        case _:
            return