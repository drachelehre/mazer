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
        def project(poly, axis):
            dots = [p.dot(axis) for p in poly]
            return min(dots), max(dots)

        for polygon in [self, other]:
            for i in range(len(polygon)):
                p1 = polygon[i]
                p2 = polygon[(i + 1) % len(polygon)]
                edge = p2 - p1
                axis = pygame.Vector2(-edge.y, edge.x).normalize()
                min1, max1 = project(self, axis)
                min2, max2 = project(other, axis)

                if max1 < min2 or max2 < min1:
                    return False  # Separating axis found

        return True

