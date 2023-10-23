import pygame

class Player:
    INITIAL_SPEED = 5
    def __init__(self, color, x, y, movement_keys):
        self.speed = Player.INITIAL_SPEED
        self.color = color
        self.set_position(x, y)
        self.size = 16
        self.movement_keys = movement_keys

    def set_position(self, x, y):
        self.pos = pygame.Vector2(x, y)
