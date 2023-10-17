import pygame
from game import Game
from Direction import Direction

class Player:
    def __init__(self, speed, color, player_pos, size, player_range, movement_keys):
        self.speed = speed
        self.color = color
        self.player_pos = player_pos
        self.size = size
        self.player_range = player_range
        self.movement_keys = movement_keys

    def draw_player(self, screen):
        pygame.draw.circle(screen, self.color, self.player_pos, self.size, self.player_range)

    def get_next_pos(self, direction):
        x = self.player_pos.x
        y = self.player_pos.y
        if direction == Direction.UP:
            y -= self.speed
        elif direction == Direction.DOWN:
            y += self.speed
        elif direction == Direction.LEFT:
            x -= self.speed
        if direction == Direction.RIGHT:
            x += self.speed

        return (x, y)

    
    