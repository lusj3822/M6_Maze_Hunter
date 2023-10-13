import pygame
from enum import Enum

pygame.init()

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

PLAYER_RADIUS = 10
MOVE_AMOUNT = 5
PLAYER_RANGE = 20

WIDTH = 1280
HEIGHT = 720
FPS = 60


text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def is_black(color):
        return color.r == 0 and color.g == 0 and color.b == 0


def distance_between_players():
    dist = pygame.math.Vector2(player_pos.x, player_pos.y).distance_to((player_pos2.x,player_pos2.y))
    return dist

def check_game_over():
    if distance_between_players() < PLAYER_RANGE:
        game_over()

def game_over():
    draw_text("Defeat", text_font, (255,0,0), (WIDTH/2) - 30, HEIGHT/2)
    player_1.color = (0,0,0)
    player_2.color = (0,0,0)


def get_color_at(x, y):
    return screen.get_at([int(x), int(y)])

def get_next_pos(current_pos, direction):
    x = current_pos.x
    y = current_pos.y
    if direction == Direction.UP:
        y -= MOVE_AMOUNT
    elif direction == Direction.DOWN:
        y += MOVE_AMOUNT
    elif direction == Direction.LEFT:
        x -= MOVE_AMOUNT
    if direction == Direction.RIGHT:
        x += MOVE_AMOUNT

    return (x, y)


def is_valid_position(x, y):
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
    next_x, next_y = get_next_pos(player_pos, direction)
    if is_valid_position(next_x, next_y):
        player_pos.x = next_x
        player_pos.y = next_y
        
    

class Player:
    def __init__(self, speed, color, player_pos, size, player_range):
        self.speed = speed
        self.color = color
        self.player_pos = player_pos
        self.size = size
        self.player_range = player_range

    def draw_player(self):
        pygame.draw.circle(screen, self.color, self.player_pos, self.size, self.player_range)

def player_movement(keys, player_pos):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move(player_pos, Direction.UP)
    if keys[pygame.K_s]:
        move(player_pos, Direction.DOWN)
    if keys[pygame.K_a]:
        move(player_pos, Direction.LEFT)
    if keys[pygame.K_d]:
        move(player_pos, Direction.RIGHT)

def player2_movement(keys, player_pos):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move(player_pos, Direction.UP)
    if keys[pygame.K_DOWN]:
        move(player_pos, Direction.DOWN)
    if keys[pygame.K_LEFT]:
        move(player_pos, Direction.LEFT)
    if keys[pygame.K_RIGHT]:
        move(player_pos, Direction.RIGHT)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
maze = pygame.image.load("maze_1.png").convert()
maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))

player_pos = pygame.Vector2(screen.get_width() / 2 - 50, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2 - 100, screen.get_height() / 2)

player_1 = Player(MOVE_AMOUNT, "red", player_pos, PLAYER_RADIUS, PLAYER_RANGE)
player_2 = Player(MOVE_AMOUNT, "blue", player_pos2, PLAYER_RADIUS, PLAYER_RANGE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(maze, (0, 0))
    # pygame.draw.circle(screen, "red", player_pos, PLAYER_RADIUS)

    distance_between_players()
    check_game_over()

    keys = pygame.key.get_pressed()

    player_1.draw_player()
    player_2.draw_player()
    player_movement(keys, player_pos)
    player2_movement(keys, player_pos2)

    
    

    pygame.display.flip()
    dt = clock.tick(FPS)
    

pygame.quit()
