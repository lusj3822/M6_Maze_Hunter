import pygame
from Direction import Direction

class Player:
    def __init__(self, color, x, y, movement_keys):
        self.speed = 5
        self.color = color
        self.set_position(x, y)
        self.radius = 7
        self.range = 15
        self.movement_keys = movement_keys

    def set_position(self, x, y):
        self.pos = pygame.Vector2(x, y)

    def get_next_pos(self, direction):
        x = self.pos.x
        y = self.pos.y
        if direction == Direction.UP:
            y -= self.speed
        elif direction == Direction.DOWN:
            y += self.speed
        elif direction == Direction.LEFT:
            x -= self.speed
        if direction == Direction.RIGHT:
            x += self.speed

        return (x, y)
