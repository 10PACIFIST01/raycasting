import pygame
import math


class Player:
    def __init__(self):
        self.x = 599
        self.y = 567
        self.speed = 2

        self.angle = 0
        self.rotation_speed = 0.02

    @property
    def pos(self):
        return (self.x, self.y)

    def move(self):
        self.sin_a = math.sin(self.angle)
        self.cos_a = math.cos(self.angle)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.x += self.speed * self.cos_a
            self.y += self.speed * self.sin_a
        if key_pressed[pygame.K_s]:
            self.x += -self.speed * self.cos_a
            self.y += -self.speed * self.sin_a
        if key_pressed[pygame.K_a]:
            self.x += self.speed * self.sin_a
            self.y += -self.speed * self.cos_a
        if key_pressed[pygame.K_d]:
            self.x += -self.speed * self.sin_a
            self.y += self.speed * self.cos_a

        if key_pressed[pygame.K_RIGHT]:
            self.angle += self.rotation_speed
        if key_pressed[pygame.K_LEFT]:
            self.angle -= self.rotation_speed