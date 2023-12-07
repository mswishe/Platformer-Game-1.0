import pygame
from objects.object import Object
from scenes.blockType import get_block

class Block(Object):
    def __init__(self, x, y, size, type):
        super().__init__(x, y, size, size)

        block = get_block(size, type)
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)