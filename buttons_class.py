import pygame
from screen import screen

pygame.init()

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_for_pressing(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos): 
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action

    def is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)
