# wall.py
import pygame
from entity import *


class Wall(Entity):
    containers = ()

    def __init__(self, x, y, width, height, rotation=0):
        super().__init__(x, y, 0)  # position is center of wall
        self.width = width
        self.height = height
        self.rotation = rotation
        self.add(*self.containers)

    def wall_shape(self):
        half_width = self.width / 2
        half_height = self.height / 2

        corners = [
            pygame.Vector2(-half_width, -half_height),
            pygame.Vector2(half_width, -half_height),
            pygame.Vector2(half_width, half_height),
            pygame.Vector2(-half_width, half_height),
        ]

        return [self.position + corner.rotate(self.rotation) for corner in corners]

    def draw(self, screen):
        pygame.draw.polygon(screen, "gray", self.wall_shape())
