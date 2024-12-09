import pygame
import math
from screen import SCREEN_WIDTH, screen
from player_settings import jumping, player_y, player
from other import run, in_game_over_screen
from game_over import game_over_screen
from fonts import font1

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Jumping parameters
gravity = 1
jump_height = 20
velocity = jump_height

# Obstacle spawn parameters
spawn_timer = 0

# Background display parameters
background = pygame.image.load("background.png").convert()
background_width = background.get_width()

# Background scroll parameters
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / background_width) + 1

# Main game loop
while run and not in_game_over_screen:

    clock.tick(FPS)

    if in_game_over_screen:
        break

    spawn_timer += 1

    # Event handler
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # Check for keys pressed
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE] and on_ground:
        jumping = True
        on_ground = False
        velocity = jump_height 
        print("SPACE")

    # Background scrolling
    for i in range(0, tiles):
        screen.blit(background, (i * background_width + scroll, 0))

    scroll -= 5

    # Obstacle spawning
    if spawn_timer >= 120:
        from game_data import spawn_obstacle
        spawn_obstacle()
        spawn_timer = 0
    from game_data import update_obstacles
    update_obstacles(screen)

    # Check for game over and display check for game over
    from obstacles_spawning import check_for_game_over
    if check_for_game_over():
        game_over_screen(screen, font1)
        run = False
                
    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    # Jumping
    if jumping:
        velocity -= gravity
        player_y -= velocity

        if velocity <= -jump_height:
            jumping = False
            velocity = 0

    elif not jumping:
        if player_y < 400:
            velocity += gravity
            player_y += velocity

        if player_y >= 400:
            player_y = 400
            on_ground = True
            velocity = 0

    player.y = player_y

    # Background scrolling
    if abs(scroll) > background_width:
        scroll = 0

    

    pygame.display.update()

pygame.quit()