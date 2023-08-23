import pygame
import math
from map import world_map, tile

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = DIST * tile
SCALE = 1200 // NUM_RAYS
TEXTURE_SIZE = 1200
TEXTURE_SCALE = TEXTURE_SIZE // tile

def mapping(a, b):
    return (a // tile) * tile, (b // tile) * tile


def ray_casting(sc, player_pos, player_angle, texture):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + tile, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, 1200, tile):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            if mapping(x + dx, yv) in world_map:
                break
            x += dx * tile

        # horizontals
        y, dy = (ym + tile, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, 800, tile):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            if mapping(xh, y + dy) in world_map:
                break
            y += dy * tile

        depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % tile
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.000001)
        proj_height = min(int(PROJ_COEFF / depth), 2 * 800)
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 2)
        pygame.draw.rect(sc, color, (ray * SCALE, 400 - proj_height // 2, SCALE, proj_height))

        wall_column = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_SIZE)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, 400 - proj_height // 2))

        cur_angle += DELTA_ANGLE