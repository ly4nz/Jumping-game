import pygame
import math
from screen import SCREEN_WIDTH, screen
from player_settings import jumping, player_y, player
from buttons import Button
from obstacles import obstacles, spawn_obstacle, update_obstacles
from game_over import in_game_over_screen, game_over_screen

pygame.init()

# Game settings
FPS = 60
clock = pygame.time.Clock()

run = True
game_over = False
on_ground = True  

# Jumping parameters
gravity = 1
jump_height = 20
velocity = jump_height

# Obstacle spawn parameters
spawn_timer = 0

# Background display parameters
background = pygame.image.load("assets/background/background.png").convert()
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
        spawn_obstacle()
        spawn_timer = 0

    # Update obstacles on screen
    update_obstacles(screen)

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Jumping mechanics
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
            jumping = False  # Reset jumping state when player hits the ground

    player.y = player_y

    # Background scrolling reset
    if abs(scroll) > background_width:
        scroll = 0

    # Check for collision and game over
    def check_for_collision():
        for obstacle in obstacles:
            if player.colliderect(obstacle["rect"]):
                game_over_screen()  # Call the game over screen
                

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display
    pygame.display.update()

pygame.quit()
