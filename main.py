import pygame
from constants import *
from entity import *
from player import *
from wall import *
from mazefield import *
from finish_flag import *
import random



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    finish_flag = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Wall.containers = (walls, updatable, drawable)
    MazeField.containers = updatable
    FinishFlag.containers = (finish_flag, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = MazeField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()