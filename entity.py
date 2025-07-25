import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.size = size

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        return pygame.Vector2.distance_to(self.position, other.position) < (self.size + other.radius)

