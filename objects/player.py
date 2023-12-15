import pygame
from scenes.spriteSheets import load_sprite_sheet

class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    ANIMATION_DELAY = 4
    SPRITES = load_sprite_sheet('Main Characters', 'Ninja Frog', 32, 32, True)

    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8 
        self.animation_count = 0
        self.jump_count += 1
        
        if self.jump_count == 1:
            self.fall_count = 0

    def hit_head(self):
        self.fall_count = 0
        self.y_vel *= -1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = 'Idle'
        if self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = 'Jump'
            elif self.jump_count == 2:
                sprite_sheet = 'Double Jump'
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = 'Fall'
        elif self.x_vel != 0:
            sprite_sheet = 'Run'

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))