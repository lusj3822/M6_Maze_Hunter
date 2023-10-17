import pygame
from Direction import Direction

class Game:
    def __init__(self, screen, players):
          self.screen = screen
          self.players = players
          
    
    def move(self, player, direction):
        next_x, next_y = player.get_next_pos(direction)
        if self.is_valid_position(next_x, next_y, player.size):
            player.player_pos.x = next_x
            player.player_pos.y = next_y

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


    def is_valid_position(self, x, y, PLAYER_RADIUS):
        up_color = self.get_color_at(x, y - PLAYER_RADIUS)
        down_color = self.get_color_at(x, y + PLAYER_RADIUS)
        right_color = self.get_color_at(x + PLAYER_RADIUS, y)
        left_color = self.get_color_at(x - PLAYER_RADIUS, y)
        if (is_black(up_color) or
                is_black(down_color) or
                is_black(left_color) or
                is_black(right_color)):
            return False
        
        return True
    
    def get_color_at(self, x, y):
        return self.screen.get_at([int(x), int(y)])

def is_black(color):
        return color.r == 0 and color.g == 0 and color.b == 0


def distance_between_players(player1, player2):
    dist = pygame.math.Vector2(player1.player_pos.x, player1.player_pos.y).distance_to((player2.player_pos.x, player2.player_pos.y))
    return dist
        
    
def is_game_over(player1, player2, PLAYER_RANGE):
    if distance_between_players(player1, player2) <= PLAYER_RANGE:
        return True
    
    if player1.player_pos.y < PLAYER_RANGE or player2.player_pos.y < PLAYER_RANGE:
        return True
    
    _, height = pygame.display.get_surface().get_size()
    if player1.player_pos.y > height - PLAYER_RANGE or player2.player_pos.y > height - PLAYER_RANGE:
        return True
    
    return False



