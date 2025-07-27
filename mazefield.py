import pygame

from constants import *
from wall import *
from player import Player
from random import *


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

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.spawn_timer = 0.0

    def spawn(self, x, y, width, height, rotation):
        wall = Wall(x, y, width, height, rotation)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > WALL_SPAWN_RATE:
            self.spawn_timer = 0  # Reset the timer

            # Spawn in front of player
            player_pos = self.player.get_position()
            player_forward = pygame.Vector2(0, 1).rotate(self.player.rotation)  # player forward vector
            spawn_distance = 10  # distance in front of player

            wall_pos = player_pos + player_forward * spawn_distance
            wall_rotation = randint(0, 360)  # optional: random rotation

            self.spawn(wall_pos.x, wall_pos.y, WALL_WIDTH, WALL_LENGTH, wall_rotation)






