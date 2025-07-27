import pygame.draw

from entity import *
from constants import *
from player import *


class Drill(Entity):
    containers = ()

    def __init__(self, x, y, size, player,):
        super().__init__(x, y, size)
        self.x = x
        self.y = y
        self.rotation = 0
        self.add(*self.containers)
        self.player = player

    def triangle(self):
        up = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.size / 1.5
        a = self.position + up * self.size
        b = self.position - up * self.size - right
        c = self.position - up * self.size + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.triangle())

    def pick_up(self):
        self.kill()
        self.player.drill_state = True


