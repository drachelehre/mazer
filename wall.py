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

    def polygon(self):
        half_w = self.width / 2
        half_h = self.height / 2

        corners = [
            pygame.Vector2(-half_w, -half_h),
            pygame.Vector2( half_w, -half_h),
            pygame.Vector2( half_w,  half_h),
            pygame.Vector2(-half_w,  half_h),
        ]

        return [self.position + corner.rotate(self.rotation) for corner in corners]

    def draw(self, screen):
        pygame.draw.polygon(screen, "gray", self.polygon())
