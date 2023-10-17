import pygame
from player import Player
from game import *

pygame.init()


MOVE_AMOUNT = 5
PLAYER_RADIUS = 7
PLAYER_RANGE = 15

WIDTH = 749
HEIGHT = 749
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
maze = pygame.image.load("maze_3.png").convert()
maze = pygame.transform.scale(maze, (WIDTH, HEIGHT))

def draw_game_over_screen():
   font = pygame.font.SysFont('arial', 40)
   title = font.render('Game Over', True, ("red"))
   restart_button = font.render('Press Esc to restart', True, ("red"))
   screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/3))
   screen.blit(restart_button, (WIDTH/2 - restart_button.get_width()/2, HEIGHT/1.9 + restart_button.get_height()))
   pygame.display.update()


text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


player_pos = pygame.Vector2(screen.get_width() / 2 - 50, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2 - 100, screen.get_height() / 2)

keys = pygame.key.get_pressed()
player_1 = Player(MOVE_AMOUNT, "red", player_pos, PLAYER_RADIUS, PLAYER_RANGE, [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])
player_2 = Player(MOVE_AMOUNT, "blue", player_pos2, PLAYER_RADIUS, PLAYER_RANGE, [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

game = Game(screen, [player_1, player_2])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(maze, (0, 0))
    keys = pygame.key.get_pressed()
    player_1.draw_player(screen)
    player_2.draw_player(screen)

    distance_between_players(player_1, player_2)

    game_over = is_game_over(player_1, player_2, PLAYER_RANGE)
    if not game_over:
        game.player_movement(player_1)
        game.player_movement(player_2)
    else:
        draw_game_over_screen()
    if keys[pygame.K_ESCAPE]:
        #running = False
        player_pos = pygame.Vector2(screen.get_width() / 2 - 50, screen.get_height() / 2)
        player_1.player_pos = player_pos

        player_pos2 = pygame.Vector2(screen.get_width() / 2 - 100, screen.get_height() / 2)
        player_2.player_pos = player_pos2
            
        
    pygame.display.flip()
    dt = clock.tick(FPS)

    

pygame.quit()
