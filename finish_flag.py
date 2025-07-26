import pygame
from entity import *
from constants import *


class FinishFlag(Entity):
    containers = ()
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, max(width, height))
        self.width = width
        self.height = height
        self.add(*self.containers)
        self.timer = 0

    def flag_shape(self):
        up = pygame.Vector2(0, -1)  # Y-axis goes down in screen coordinates
        right = pygame.Vector2(1, 0)

        pole_top = self.position + up * self.width

        a = self.position + right * self.height
        b = self.position
        c = pole_top
        d = pole_top + right * self.height

        return [a, b, c, d]

    def draw(self, screen):
        pygame.draw.polygon(screen, "green", self.flag_shape())

