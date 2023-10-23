import pygame
from player import Player
from game import Game

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == Game.SPAWN_POWERUP:
            game.create_powerup()

    game.refresh_maze()    
    game.draw_player(game.player1)
    game.draw_player(game.player2)
    game.draw_powerup()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        game.draw_fog_of_war()

    for player in [game.player1, game.player2]:
        player_rect = pygame.Rect((int(player.pos.x), int(player.pos.y)), (player.size, player.size))
        if game.powerup != None and player_rect.colliderect(game.powerup):
            player.speed += 1
            game.powerup = None

    game_over = game.is_game_over()
    if not game_over:
        game.player_movement(game.player1)
        game.player_movement(game.player2)
    else:
        game.draw_game_over_screen()
        if keys[pygame.K_ESCAPE]:
            game.reset()
            
        
    pygame.display.flip()
    clock.tick(FPS)
    

    
pygame.quit()
