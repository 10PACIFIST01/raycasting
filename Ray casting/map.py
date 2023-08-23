import pygame

text_map = [
    "wwwwwwwwwwww",
    "w..........w",
    'w..w...w...w',
    'w..wwwww...w',
    'w..w...w...w',
    'w..w...w...w',
    "w..........w",
    "wwwwwwwwwwww"
]
world_map = set()
mini_map = set()
tile = 100
MAP_SCALE = 5
MAP_TILE = tile // MAP_SCALE

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "w":
            world_map.add((i * tile, j * tile))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))