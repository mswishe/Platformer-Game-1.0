from objects.block import Block
import global_variables as gv

def create_scene_one():
    floor = [Block(i * gv.BLOCK_SIZE, gv.HEIGHT - gv.BLOCK_SIZE, gv.BLOCK_SIZE, 'greenGrass') for i in range(-gv.WIDTH // gv.BLOCK_SIZE, (gv.WIDTH * 2) // gv.BLOCK_SIZE)]

    objects = [*floor, Block(gv.WIDTH - (gv.BLOCK_SIZE * 2), gv.HEIGHT - (gv.BLOCK_SIZE * 2), gv.BLOCK_SIZE, 'greenGrass')]

    return objects