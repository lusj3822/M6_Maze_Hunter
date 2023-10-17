import pygame
from player import Player
from game import *


FPS = 60
WIDTH = 749
HEIGHT = 749
player_1_start_x = WIDTH / 2 - 50
player_1_start_y = HEIGHT / 2
player_2_start_x = WIDTH / 2 - 100
player_2_start_y = HEIGHT / 2

player_1 = Player("red", player_1_start_x, player_1_start_y, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
player_2 = Player("blue", player_2_start_x, player_2_start_y, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

pygame.init()
game = Game(WIDTH, HEIGHT, player_1, player_2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.refresh_maze()    
    game.draw_player(player_1)
    game.draw_player(player_2)

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
            player_1.set_position(player_1_start_x, player_1_start_y)
            player_2.set_position(player_2_start_x, player_2_start_y)
            
        
    pygame.display.flip()
    game.clock.tick(FPS)
    

    
pygame.quit()
