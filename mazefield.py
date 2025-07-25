import pygame
from constants import *
from wall import *


class MazeField(pygame.sprite.Sprite):
    containers = ()

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-WALL_MAX_LENGTH, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + WALL_MAX_LENGTH, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -WALL_MAX_LENGTH),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + WALL_MAX_LENGTH
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, size, position):
        wall = Wall(position.x, position.y, size)






