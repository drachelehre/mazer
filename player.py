import pygame
from entity import *
from constants import *


class Player(Entity):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SIZE)
        self.last_move_vec = None
        self.rotation = 0
        self.add(*self.containers)
        self.timer = 0

    def triangle(self):
        up = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.size / 1.5
        a = self.position + up * self.size
        b = self.position - up * self.size - right
        c = self.position - up * self.size + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        return forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        move_vec = pygame.Vector2(0, 0)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move_vec += self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move_vec -= self.move(dt)

        self.position += move_vec
        self.last_move_vec = move_vec  # store for sliding correction

        # game boundary resolution, no more wandering offscreen
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

