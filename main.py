import pygame
from player import Player
from game import *


FPS = 60
WIDTH = 749
HEIGHT = 749
PLAYER_1_START_X = 300
PLAYER_1_START_Y = 370
PLAYER_2_START_X = 250
PLAYER_2_START_Y = 370

player_1 = Player("red", PLAYER_1_START_X, PLAYER_1_START_Y, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
player_2 = Player("blue", PLAYER_2_START_X, PLAYER_2_START_Y, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
game = Game(WIDTH, HEIGHT, player_1, player_2)

pygame.init()
SPAWN_POWERUP_EVENT = pygame.USEREVENT
pygame.time.set_timer(SPAWN_POWERUP_EVENT, 10000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_POWERUP_EVENT:
            game.create_powerup()

    game.refresh_maze()    
    game.draw_player(player_1)
    game.draw_player(player_2)
    game.draw_powerup()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        game.draw_fog_of_war()


    game_over = game.is_game_over()
    if not game_over:
        game.player_movement(player_1)
        game.player_movement(player_2)
    else:
        game.draw_game_over_screen()
        if keys[pygame.K_ESCAPE]:
            player_1.set_position(PLAYER_1_START_X, PLAYER_1_START_Y)
            player_2.set_position(PLAYER_2_START_X, PLAYER_2_START_Y)
            
        
    pygame.display.flip()
    game.clock.tick(FPS)
    

    
pygame.quit()
