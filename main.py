import pygame
import global_variables as gv
from scenes.background import get_background
from scenes.sceneOne import create_scene_one

pygame.init()
pygame.display.set_caption("Platformer")

gv.init()

window = pygame.display.set_mode((gv.WIDTH, gv.HEIGHT))

def draw(window, background, bg_image, objects):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window)

    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    scene_one_objects = create_scene_one()

    run = True
    while(run):
        clock.tick(gv.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image, scene_one_objects)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)