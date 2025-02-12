import pygame
from screen import screen
from buttons import Button

pygame.init()

white = (255, 255, 255)

# Game state flags
run = True  # Add this so the main game loop can run
in_game_over_screen = False  # Initially true to show the game over screen
game_over = False

# Button setup
exit_button_img = pygame.image.load("assets/buttons/exit.png").convert_alpha()
exit_button = Button(100, 200, exit_button_img)
retry_button_img = pygame.image.load("assets/buttons/retry.png").convert_alpha()
retry_button = Button(100, 400, retry_button_img)

def game_over_screen():
    global in_game_over_screen, run  # Declare the global variables

    while in_game_over_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Stop the game
                in_game_over_screen = False  # Exit the game over screen

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if exit button is clicked
                pos = pygame.mouse.get_pos()
                if exit_button.is_clicked(pos):
                    run = False
                    in_game_over_screen = False

                # Check if retry button is clicked
                if retry_button.is_clicked(pos):
                    print("Retrying...")  # Implement retry logic here
                    in_game_over_screen = False  # Exit the game over screen

        # Fill screen with white
        screen.fill(white)

        # Draw buttons
        exit_button.draw()
        retry_button.draw()

        # Update the display
        pygame.display.update()

# Main game loop
while run:
    # You may put your game logic here

    # Show game over screen if game over condition is met
    if game_over:
        game_over_screen()  # Call the game over screen function

    pygame.time.delay(100)  

