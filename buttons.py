import pygame
from screen import screen
from buttons_class import Button
pygame.init()

exit_button_img = pygame.image.load("exit.png").convert_alpha()
retry_button_img = pygame.image.load("retry.png").convert_alpha()


exit_button = Button(100, 200, exit_button_img)
retry_button = Button(500, 200, retry_button_img)

def draw_buttons(button):
    button.draw()



