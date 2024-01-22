import pygame
from objects.object import Object
from scenes.spriteSheets import load_sprite_sheet

class End(Object):
    ANIMATION_DELAY = 4
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "end")

        self.end = load_sprite_sheet("Checkpoints", "End", width, height)
        self.image = self.end["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"

    def loop(self):
        sprites = self.end[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0