import pygame
from entity import *
from constants import *
from player import *


class FinishFlag(Entity):
    containers = ()
    
    def __init__(self, x, y, width, height, player):
        super().__init__(x, y, max(width, height))
        self.width = width
        self.height = height
        self.add(*self.containers)
        self.timer = 0
        self.player = player
        self.last_move_vec = None

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

    def update(self, dt):
        move_vec = pygame.Vector2(0, 0)

        escape_direction = self.position - self.player.position
        distance = escape_direction.length()

        if SAFE_DISTANCE > distance > 0:
            escape_direction.normalize_ip()
            move_vec += escape_direction * FLAG_SPEED * dt

        self.position += move_vec
        self.last_move_vec = move_vec

        bounced = False
        normal = None

        if self.position.x < self.size:
            self.position.x = self.size
            normal = pygame.Vector2(1, 0)
            bounced = True
        elif self.position.x > SCREEN_WIDTH - self.size:
            self.position.x = SCREEN_WIDTH - self.size
            normal = pygame.Vector2(-1, 0)
            bounced = True

        if self.position.y < self.size:
            self.position.y = self.size
            normal = pygame.Vector2(0, 1)
            bounced = True
        elif self.position.y > SCREEN_HEIGHT - self.size:
            self.position.y = SCREEN_HEIGHT - self.size
            normal = pygame.Vector2(0, -1)
            bounced = True

        if bounced and self.last_move_vec.length() > 0:
            reflect = self.last_move_vec.reflect(normal)
            self.position += reflect * 0.5
