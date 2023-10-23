import pygame
from random import randrange
from Direction import Direction

class Game:
    POWERUP_RADIUS = 7
    def __init__(self, width, height, player1, player2):
          self.screen = pygame.display.set_mode((width, height))
          self.maze = pygame.image.load("maze_3.png").convert()
          self.maze = pygame.transform.scale(self.maze, (width, height))
          pygame.display.set_caption("Maze Hunter")
          self.clock = pygame.time.Clock()
          self.player1 = player1
          self.player2 = player2
          self.powerup = None

    def refresh_maze(self):
        self.screen.blit(self.maze, (0, 0))

    def draw_fog_of_war(self):
        surface1 = self.screen.convert_alpha()
        fog_of_war_size = 50

        pygame.draw.circle(surface1, (0, 0, 0, 255), (0, 0), 2000) # GIGANTISK SVART CIRKEL SOM GÖR ALLTING SVART
        for player in [self.player1, self.player2]:
            pygame.draw.circle(surface1, (255, 0, 0, 0), (player.pos.x, player.pos.y), fog_of_war_size)

        self.screen.blit(surface1, (0,0))

    def draw_powerup(self):
        if self.powerup != None:
            pygame.draw.rect(self.screen, "green", self.powerup)

    def create_powerup(self):
        while True:
            x, y = self.get_random_location()
            if self.is_valid_position(x, y, Game.POWERUP_RADIUS):
                self.powerup = pygame.Rect(
                        (x - Game.POWERUP_RADIUS, y - Game.POWERUP_RADIUS),
                        (Game.POWERUP_RADIUS * 2, Game.POWERUP_RADIUS * 2))
                return

    def get_random_location(self):
        x = randrange(self.screen.get_width());
        y = randrange(self.screen.get_height());
        return x, y

    def draw_player(self, player):
        pygame.draw.circle(self.screen, player.color, player.pos, player.radius, player.range)
          
    def draw_game_over_screen(self):
       font = pygame.font.SysFont('arial', 40)
       title = font.render('Game Over', True, ("red"))
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
        next_x, next_y = player.get_next_pos(direction)
        if self.is_valid_position(next_x, next_y, player.radius):
            player.pos.x = next_x
            player.pos.y = next_y

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


    def is_valid_position(self, x, y, object_radius):
        up = (x, y - object_radius)
        down = (x, y + object_radius)
        right = (x + object_radius, y)
        left = (x - object_radius, y)
        for x, y in [up, down, right, left]:
            if self.is_outside_maze(x, y) or is_black(self.get_color_at(x, y)): 
                return False
        return True

    def is_outside_maze(self, x, y):
        return (x < 0 
                or x > self.screen.get_width() - 1 
                or y < 0 
                or y > self.screen.get_height() - 1)


    def is_game_over(self):
        if self.distance_between_players() <= (self.player1.range or self.player2.range):
            return True
        
        if self.player1.pos.y < self.player1.range or self.player2.pos.y < self.player2.range:
            return True
        
        height = self.screen.get_height()
        if self.player1.pos.y > height - self.player1.range or self.player2.pos.y > height - self.player2.range:
            return True
        
        return False

    def distance_between_players(self):
        return self.player1.pos.distance_to(self.player2.pos)
        
    def get_color_at(self, x, y):
        return self.screen.get_at([int(x), int(y)])

def is_black(color):
        return color.r == 0 and color.g == 0 and color.b == 0
