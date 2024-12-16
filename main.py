import pygame
import math
from screen import SCREEN_WIDTH, screen
from player_settings import jumping, player_y, player
from other import run, in_game_over_screen
from buttons import Button
from obstacles_spawning import obstacles
from game_data import spawn_obstacle, update_obstacles

pygame.init()

# Game settings
FPS = 60
clock = pygame.time.Clock()

game_over = False
on_ground = True  # Initialize on_ground flag to True

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

# Button setup
exit_button_img = pygame.image.load("exit.png").convert_alpha()
exit_button = Button(100, 200, exit_button_img)  # Position your exit button

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

    player.y = player_y

    # Background scrolling reset
    if abs(scroll) > background_width:
        scroll = 0

    # Check for collision and game over
    def check_for_collision():
        for obstacle in obstacles:
            if player.colliderect(obstacle["rect"]):
                return True
        return False  # Ensure the function returns a boolean

    if check_for_collision():
        game_over = True

    if game_over:
        exit_button.draw()  # Draw the exit button when game is over

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display
    pygame.display.update()

pygame.quit()
