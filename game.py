import pygame
from enum import Enum
from random import randrange
from player import Player
import random

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class GameState(Enum):
    PLAYING = 0
    HUNTER_WON = 1
    PRISONER_WON = 2

class Game:
    POWERUP_SIZE = 14
    SPAWN_POWERUP = pygame.USEREVENT

    def __init__(self, width, height, player1, player2):
          self.screen = pygame.display.set_mode((width, height))
          self.maze = pygame.image.load("maze_3.png").convert()
          self.maze = pygame.transform.scale(self.maze, (width, height))
          self.rotate_maze();
          self.player1 = player1
          self.player2 = player2
          pygame.time.set_timer(Game.SPAWN_POWERUP, 10000)
          self.powerup = None

    def start(self):
        self.game_state = GameState.PLAYING
        x1, y1 = self.get_random_valid_location(self.player1.size)
        x2, y2 = self.get_random_valid_location(self.player2.size)
        self.player1.set_position(x1, y1)
        self.player2.set_position(x2, y2)

    def reset(self):
        self.player1.speed = Player.INITIAL_SPEED
        self.player2.speed = Player.INITIAL_SPEED
        self.powerup = None
        self.start()

    def refresh_maze(self):
        self.screen.blit(self.maze, (0, 0))

    def rotate_maze(self):
        degrees_of_rotation = [0, 90, 180, 270]
        self.maze = pygame.transform.rotate(self.maze, random.choice(degrees_of_rotation))
        self.refresh_maze()

    def draw_fog_of_war(self):
        surface1 = self.screen.convert_alpha()
        fog_of_war_size = 50

        pygame.draw.circle(surface1, (0, 0, 0, 255), (0, 0), 2000) # GIGANTISK SVART CIRKEL SOM GÖR ALLTING SVART
        for player in [self.player1, self.player2]:
            pygame.draw.circle(surface1, (255, 0, 0, 0), (player.pos.x, player.pos.y), fog_of_war_size)

        self.screen.blit(surface1, (0,0))

    def draw_powerup(self):
        if self.powerup != None:
            pygame.draw.rect(self.screen, "darkgreen", self.powerup)

    def create_powerup(self):
        x, y = self.get_random_valid_location(Game.POWERUP_SIZE) 
        self.powerup = pygame.Rect(
                    (int(x), int(y)),
                    (Game.POWERUP_SIZE, Game.POWERUP_SIZE))

    def get_random_valid_location(self, object_size):
        while True:
            x, y = self.get_random_location()
            if self.is_valid_position(x, y, object_size):
                return x, y


    def get_random_location(self):
        x = randrange(self.screen.get_width());
        y = randrange(self.screen.get_height());
        return x, y

    def draw_player(self, player):
        pygame.draw.rect(self.screen, player.color, pygame.Rect(player.pos, (player.size, player.size)))
          
    def draw_start_screen(self):
        start_screen_image = pygame.image.load("maze_menu_screen.png")
        start_screen_image = pygame.transform.scale(start_screen_image, (749,749))
        self.screen.blit(start_screen_image, (0,0))
        width = self.screen.get_width()
        height = self.screen.get_height()
        title_font = pygame.font.SysFont('arial', 60)
        option_font = pygame.font.SysFont('arial', 40)
        game_title = title_font.render("Maze Hunter", True, ("white"))
        light_mode = option_font.render("1: Light mode", True, ("white"))
        dark_mode = option_font.render("2: Dark mode", True, ("White"))
        quit_option = option_font.render("3: Quit", True, ("white"))
        self.screen.blit(game_title, ((width/2 - game_title.get_width()/2), (height/4)) )
        self.screen.blit(light_mode, ((width/2 - light_mode.get_width()/2), (height/2.5)))
        self.screen.blit(dark_mode, ((width/2 - dark_mode.get_width()/2), (height/2)))
        self.screen.blit(quit_option, ((width/2 - quit_option.get_width()/2), (height/1.5)))
        pygame.display.update()


    def draw_game_over_screen(self, text):
       font = pygame.font.SysFont('arial', 40)
       title = font.render(text, True, ("red"))
       restart_button = font.render('Press Esc to restart', True, ("red"))
       width = self.screen.get_width();
       height = self.screen.get_height();
       self.screen.blit(title, (width/2 - title.get_width()/2, height/2 - title.get_height()/3))
       self.screen.blit(restart_button, (width/2 - restart_button.get_width()/2, height/1.9 + restart_button.get_height()))
       pygame.display.update()

    def draw_text(self, text, color, x, y):
        font = pygame.font.SysFont("Arial", 30)
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))
    
    def move(self, player, direction):
        x_diff = 0
        y_diff = 0
        if direction == Direction.UP:
            y_diff = -1
        elif direction == Direction.DOWN:
            y_diff = 1
        elif direction == Direction.LEFT:
            x_diff = -1
        elif direction == Direction.RIGHT:
            x_diff = 1

        for _ in range(player.speed):
            next_x = player.pos.x + x_diff
            next_y = player.pos.y + y_diff
            if self.is_valid_position(next_x, next_y, player.size):
                player.pos.x = next_x
                player.pos.y = next_y
            else: return

    def player_movement(self, player):
        keys = pygame.key.get_pressed()
        if keys[player.movement_keys[0]]:
            self.move(player, Direction.UP)
        if keys[player.movement_keys[1]]:
            self.move(player, Direction.DOWN)
        if keys[player.movement_keys[2]]:
            self.move(player, Direction.LEFT)
        if keys[player.movement_keys[3]]:
            self.move(player, Direction.RIGHT)


    def is_valid_position(self, x, y, size):
        top_left = (x, y)
        top_middle = (x + size / 2, y)
        top_right = (x + size, y)
        bottom_left = (x, y + size)
        bottom_middle = (x + size / 2, y + size)
        bottom_right = (x + size, y + size)
        middle_left = (x, y + size / 2)
        middle_right = (x + size, y + size / 2)
        positions = [top_left, top_middle, top_right,
                     bottom_left, bottom_middle, bottom_right,
                     middle_left, middle_right]
        for pos_x, pos_y in positions:
            if self.is_outside_maze(pos_x, pos_y) or is_black(self.get_color_at(pos_x, pos_y)): 
                return False
        return True

    def is_outside_maze(self, x, y):
        return (x < 0 
                or x > self.screen.get_width() - 1 
                or y < 0 
                or y > self.screen.get_height() - 1)

    def is_on_edge_of_maze(self, player):
        return (player.pos.x == 0 
                or player.pos.x + player.size == self.screen.get_width() - 1
                or player.pos.y == 0
                or player.pos.y + player.size == self.screen.get_height() - 1)


    def is_game_over(self):
        if self.distance_between_players() <= (self.player1.size or self.player2.size):
            self.state = GameState.HUNTER_WON
            return True

        for player in [self.player1, self.player2]:
            if self.is_on_edge_of_maze(player):
                self.state = GameState.PRISONER_WON
                return True
        
        return False

    def distance_between_players(self):
        return self.player1.pos.distance_to(self.player2.pos)
        
    def get_color_at(self, x, y):
        return self.screen.get_at([int(x), int(y)])

def is_black(color):
        return color.r == 0 and color.g == 0 and color.b == 0
