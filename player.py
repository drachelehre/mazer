import pygame
from entity import *
from constants import *


class Player(Entity):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SIZE)
        self.rotation = 0
        # Add the player instance to the specified groups
        self.add(*self.containers)
        self.timer = 0