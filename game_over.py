import pygame
from buttons import exit_button, retry_button, draw_buttons
from screen import screen
from reset_game import reset_game


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def display_game_over(screen, font_big):
    screen.fill((255, 255, 255))
    draw_text("GAME OVER!", font_big, (0, 0, 0), 350, 50)
    draw_buttons(exit_button)
    draw_buttons(retry_button)

def game_over_screen(screen, font_big):  # Add reset_game_function argument
    in_game_over_screen = True
    
    while in_game_over_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        display_game_over(screen, font_big)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if exit_button.check_for_pressing(): 
            pygame.quit()
            return

        if retry_button.check_for_pressing():  
            reset_game()
            return

        pygame.display.update()
