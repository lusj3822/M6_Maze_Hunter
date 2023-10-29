import pygame
from player import Player
from game import *

FPS = 60
WIDTH = 749
HEIGHT = 749

player1 = Player("purple4", [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
player2 = Player("firebrick", [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
game = Game(WIDTH, HEIGHT, player1, player2)
game.start()

pygame.init()
pygame.display.set_caption("Maze Hunter")
clock = pygame.time.Clock()
running = True

def game_light_mode():
    game.refresh_maze()    
    game.draw_player(game.player1)
    game.draw_player(game.player2)
    game.draw_powerup()

    for player in [game.player1, game.player2]:
        player_rect = pygame.Rect((int(player.pos.x), int(player.pos.y)), (player.size, player.size))
        if game.powerup != None and player_rect.colliderect(game.powerup):
            player.speed += 1
            game.powerup = None

    if game.is_game_over():
        if game.state == GameState.HUNTER_WON:
            game.draw_game_over_screen("Hunter won") 
        elif game.state == GameState.PRISONER_WON:
            game.draw_game_over_screen("Prisoner won")
        if keys[pygame.K_ESCAPE]:
            game.reset()
            game.rotate_maze()
    else:
        game.player_movement(game.player1)
        game.player_movement(game.player2)

def game_dark_mode():
    game.refresh_maze()    
    game.draw_player(game.player1)
    game.draw_player(game.player2)
    game.draw_powerup()
    game.draw_fog_of_war()

    for player in [game.player1, game.player2]:
        player_rect = pygame.Rect((int(player.pos.x), int(player.pos.y)), (player.size, player.size))
        if game.powerup != None and player_rect.colliderect(game.powerup):
            player.speed += 1
            game.powerup = None

    if game.is_game_over():
        if game.state == GameState.HUNTER_WON:
            game.draw_game_over_screen("Hunter won") 
        elif game.state == GameState.PRISONER_WON:
            game.draw_game_over_screen("Prisoner won")
        if keys[pygame.K_ESCAPE]:
            game.reset()
            game.rotate_maze()
    else:
        game.player_movement(game.player1)
        game.player_movement(game.player2)

menu_option = "start_screen"

game.rotate_maze()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == Game.SPAWN_POWERUP:
            game.create_powerup()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        menu_option = "start_game_light_mode"
    if keys[pygame.K_2]:
        menu_option = "start_game_dark_mode"
    if keys[pygame.K_3]:
        menu_option = "quit"

    if menu_option == "start_screen":
        game.draw_start_screen()
    if menu_option == "start_game_light_mode":
        game_light_mode()
    if menu_option == "start_game_dark_mode":
        game_dark_mode()
    
    if menu_option == "quit":
        running = False

    pygame.display.flip()
    clock.tick(FPS)
    

    
pygame.quit()