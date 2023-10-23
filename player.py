import pygame

class Player:
    INITIAL_SPEED = 5

    def __init__(self, color, movement_keys):
        self.speed = Player.INITIAL_SPEED
        self.color = color
        self.size = 16
        self.movement_keys = movement_keys

    def set_position(self, x, y):
        self.pos = pygame.Vector2(x, y)
