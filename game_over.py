import pygame
from screen import screen
from buttons import Button

pygame.init()

white = (255, 255, 255)

in_game_over_screen = False
game_over = False

# Button setup
exit_button_img = pygame.image.load("assets/buttons/exit.png").convert_alpha()
exit_button = Button(100, 200, exit_button_img)
retry_button_img = pygame.image.load("assets/buttons/retry.png").convert_alpha()
retry_button = Button(100, 400, retry_button_img)

def game_over_screen():
    global run, in_game_over_screen
    while in_game_over_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                in_game_over_screen = False  # Exit the game over screen loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    retry_button.check_click(pos)
                    exit_button.check_click(pos)

        screen.fill(white)
        exit_button.draw()
        retry_button.draw()
        pygame.display.update()


