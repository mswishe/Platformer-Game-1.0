from objects.block import Block
import global_variables as gv

def create_scene_one():
    floor = [Block(i * gv.BLOCK_SIZE, gv.HEIGHT - gv.BLOCK_SIZE, gv.BLOCK_SIZE, 'greenGrass') for i in range(1, (gv.WIDTH * 2) // gv.BLOCK_SIZE)]
    wall = [Block(0, i * gv.BLOCK_SIZE, gv.BLOCK_SIZE, 'greenGrass') for i in range(0, (gv.HEIGHT * 2) // gv.BLOCK_SIZE)]
    wall_2 = [Block(-gv.BLOCK_SIZE, i * gv.BLOCK_SIZE, gv.BLOCK_SIZE, 'greenGrass') for i in range(0, (gv.HEIGHT * 2) // gv.BLOCK_SIZE)]
    wall_end = [Block((gv.WIDTH * 2) - 22, i * gv.BLOCK_SIZE, gv.BLOCK_SIZE, 'greenGrass') for i in range(0, (gv.HEIGHT * 2) // gv.BLOCK_SIZE)]
    wall_end_2 = [Block((gv.WIDTH * 2) - 22 + gv.BLOCK_SIZE, i * gv.BLOCK_SIZE, gv.BLOCK_SIZE, 'greenGrass') for i in range(0, (gv.HEIGHT * 2) // gv.BLOCK_SIZE)]
    blocks = [Block(gv.WIDTH - (gv.BLOCK_SIZE * 7), gv.HEIGHT - (gv.BLOCK_SIZE * 5), gv.BLOCK_SIZE, 'greenGrass'), 
              Block(gv.WIDTH - (gv.BLOCK_SIZE * 3), gv.HEIGHT - (gv.BLOCK_SIZE * 3), gv.BLOCK_SIZE, 'greenGrass'),
              Block(gv.WIDTH - (gv.BLOCK_SIZE * 3), gv.HEIGHT - (gv.BLOCK_SIZE * 2), gv.BLOCK_SIZE, 'greenGrass'), 
              Block(gv.WIDTH - (gv.BLOCK_SIZE * 2), gv.HEIGHT // 2, gv.BLOCK_SIZE, 'greenGrass')]
    

    objects = [*floor, *wall, *wall_2, *wall_end, *wall_end_2, *blocks]

    return objects 