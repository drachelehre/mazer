import pygame
from random import *
from constants import *
from drill import *


def polygons_collide(poly1, poly2):
    def project(poly, axis):
        dots = [p.dot(axis) for p in poly]
        return min(dots), max(dots)

    for polygon in [poly1, poly2]:
        for i in range(len(polygon)):
            p1 = polygon[i]
            p2 = polygon[(i + 1) % len(polygon)]
            edge = p2 - p1
            axis = pygame.Vector2(-edge.y, edge.x).normalize()
            min1, max1 = project(poly1, axis)
            min2, max2 = project(poly2, axis)

            if max1 < min2 or max2 < min1:
                return False  # Separating axis found

    return True  # No separating axis → collision


def spawn_drill(player):
    padding = 50  # keep drills away from edges
    x = randint(padding, SCREEN_WIDTH - padding)
    y = randint(padding, SCREEN_HEIGHT - padding)
    size = DRILL_SIZE  # define in constants.py

    drill = Drill(x, y, size, player, DRILL_DURATION)
    return drill
