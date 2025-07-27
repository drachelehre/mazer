import pygame
from constants import *
from entity import *
from player import *
from wall import *
from mazefield import *
from finish_flag import *
import random
from utils import *
import time


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    timer = TIMER_START

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    finish_flag = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Wall.containers = (walls, updatable, drawable)
    MazeField.containers = updatable
    FinishFlag.containers = (finish_flag, updatable, drawable)

    player = Player(SCREEN_WIDTH / 10, SCREEN_HEIGHT / 10)
    finish_flag = FinishFlag(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, FLAG_WIDTH, FLAG_HEIGHT, player)
    field = MazeField(player)

    dt = 0

    for _ in range(INIT_WALL_NUM):
        x = random.randint(50, SCREEN_WIDTH - 50)
        y = random.randint(50, SCREEN_HEIGHT - 50)

        width = WALL_WIDTH
        height = random.randint(WALL_LENGTH, WALL_MAX_LENGTH)

        rotation = random.uniform(0, 360)

        Wall(x, y, width, height, rotation)

    font = pygame.font.SysFont(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        old_pos = player.position - player.last_move_vec

        collided = False

        for wall in walls:
            if polygons_collide(player.triangle(), wall.wall_shape()):
                collided = True

                # return to previous position
                player.position = old_pos

                # approximate wall position
                player_poly = player.triangle()
                wall_poly = wall.wall_shape()

                # find closest edge on wall to the player
                closest_edge = None
                min_dist = float('inf')
                for i in range(len(wall_poly)):
                    a = wall_poly[i]
                    b = wall_poly[(i + 1) % len(wall_poly)]
                    edge_center = (a + b) / 2
                    dist = player.position.distance_to(edge_center)
                    if dist < min_dist:
                        min_dist = dist
                        closest_edge = (a, b)

                if closest_edge:
                    a, b = closest_edge
                    wall_edge = (b - a).normalize()

                    # hit the wall
                    move_vec = player.last_move_vec
                    slide_vec = move_vec.project(wall_edge)

                    # apply the slide
                    player.position += slide_vec

                break

        if polygons_collide(player.triangle(), finish_flag.flag_shape()):
            print("Good job! You win!")
            return

        font = pygame.font.SysFont(None, 36)
        timer_text = font.render(f"Time: {int(timer)}", True, pygame.Color("white"))
        screen.blit(timer_text, (10, 10))
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        timer -= dt
        if timer <= 0:
            print("Time's up!")
            pygame.quit()
            return


if __name__ == "__main__":
    main()
