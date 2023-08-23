import pygame
from raycasting import *
from map import *
import math


class Drawing:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont("Arial", 18, bold=True)
        self.texture = pygame.image.load("img/wall_texture.png").convert()

    def background(self):
        pygame.draw.rect(self.screen, (0, 0, 255), (0, 0, 1200, 400))
        pygame.draw.rect(self.screen, (80, 80, 80), (0, 400, 1200, 800))

    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle, self.texture)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, (255, 0, 0))
        self.screen.blit(render, (1200 - 25, 5))

    def mini_map(self, player):
        self.screen_map.fill((0, 0, 0))
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE

        pygame.draw.circle(self.screen_map, (0, 255, 0), (int(map_x), int(map_y)), 6)
        pygame.draw.line(self.screen_map, (0, 255, 0), (map_x, map_y),
                         (map_x + MAP_TILE * math.cos(player.angle),
                          map_y + MAP_TILE * math.sin(player.angle)))

        for x, y in mini_map:
            pygame.draw.rect(self.screen_map, (0, 255, 0), (x, y, MAP_TILE, MAP_TILE))

        self.screen.blit(self.screen_map, (0, 800 - 800 // MAP_SCALE))