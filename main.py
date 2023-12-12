import pygame
import global_variables as gv

# initialize pygame display and window at the very start to avoid problems with initialization of other surfaces
pygame.init()
pygame.display.set_caption("Platformer")
gv.init()
window = pygame.display.set_mode((gv.WIDTH, gv.HEIGHT))

from scenes.background import get_background
from scenes.sceneOne import create_scene_one
from objects.player import Player

def vertical_collision(player, objects, y_vel):
    collided_objects = []

    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if y_vel > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif y_vel < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects

def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0

    if keys[pygame.K_a]:
        player.move_left(gv.PLAYER_VEL)
    if keys[pygame.K_d]:
        player.move_right(gv.PLAYER_VEL)

    vertical_collision(player, objects, player.y_vel)

def draw(window, background, bg_image, objects, player):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window)

    player.draw(window)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    player = Player(80, 80, 40, 40)

    scene_one_objects = create_scene_one()

    run = True
    while(run):
        clock.tick(gv.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(gv.FPS)
        handle_move(player, scene_one_objects)
        draw(window, background, bg_image, scene_one_objects, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)