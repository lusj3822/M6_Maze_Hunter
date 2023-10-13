import pygame
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

PLAYER_RADIUS = 10
MOVE_AMOUNT = 300

def is_black(color):
        return color.r == 0 and color.g == 0 and color.b == 0

def get_color_at(x, y):
    return screen.get_at([int(x), int(y)])

def get_next_pos(current_pos, direction):
    x = current_pos.x
    y = current_pos.y
    if direction == Direction.UP:
        y -= MOVE_AMOUNT * dt
    elif direction == Direction.DOWN:
        y += MOVE_AMOUNT * dt
    elif direction == Direction.LEFT:
        x -= MOVE_AMOUNT * dt
    if direction == Direction.RIGHT:
        x += MOVE_AMOUNT * dt
    return (x, y)

def is_valid_movement(current_pos, direction):
    x, y = get_next_pos(current_pos, direction)

    up_color = get_color_at(x, y - PLAYER_RADIUS)
    down_color = get_color_at(x, y + PLAYER_RADIUS)
    right_color = get_color_at(x + PLAYER_RADIUS, y)
    left_color = get_color_at(x - PLAYER_RADIUS, y)
    if (is_black(up_color) or
            is_black(down_color) or
            is_black(left_color) or
            is_black(right_color)):
        return False

    return True

def move(player_pos, direction):
    if is_valid_movement(player_pos, direction) == False:
        return

    if direction == Direction.UP:
        player_pos.y -= MOVE_AMOUNT * dt
    elif direction == Direction.DOWN:
        player_pos.y += MOVE_AMOUNT * dt
    elif direction == Direction.LEFT:
        player_pos.x -= MOVE_AMOUNT * dt
    elif direction == Direction.RIGHT:
        player_pos.x += MOVE_AMOUNT * dt




pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
maze = pygame.image.load("maze_1.png").convert()
maze = pygame.transform.scale(maze, (width, height))
player_pos = pygame.Vector2(screen.get_width() / 2 - 50, screen.get_height() / 2)

dt = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(maze, (0, 0))
    pygame.draw.circle(screen, "red", player_pos, PLAYER_RADIUS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move(player_pos, Direction.UP)
    if keys[pygame.K_s]:
        move(player_pos, Direction.DOWN)
    if keys[pygame.K_a]:
        move(player_pos, Direction.LEFT)
    if keys[pygame.K_d]:
        move(player_pos, Direction.RIGHT)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
