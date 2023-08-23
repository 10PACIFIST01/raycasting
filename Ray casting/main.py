import pygame
from player import Player
from map import *
from Drawing import Drawing
import math


class Game:
    def __init__(self):
        self.FPS = 60
        self.caption = "3D graphic"
        self.size = (1200, 800)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        screen_map = pygame.Surface((self.size[0] // MAP_SCALE, self.size[1] // MAP_SCALE))
        pygame.display.set_caption(self.caption)
        clock = pygame.time.Clock()
        player = Player()
        drawing = Drawing(screen, screen_map)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            player.move()
            screen.fill((40, 40, 40))

            drawing.background()
            drawing.world(player.pos, player.angle)
            drawing.fps(clock)
            drawing.mini_map(player)

            pygame.display.flip()
            clock.tick()

game = Game()
game.run()
