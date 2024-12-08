import pygame
import random
from screen import SCREEN_WIDTH, screen
from player_settings import player
from game_over import game_over_screen, retry_button, exit_button
from other import run, game_over

pygame.init()

obstacle_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

obstacles = []

def reset_obstacles():
    global obstacles
    obstacles.clear()

def spawn_obstacle():
    obstacle_color = random.choice(obstacle_colors)
    obstacle_y = 400
    obstacle = {
        "rect": pygame.Rect(SCREEN_WIDTH, obstacle_y, 25, 25),
        "color": obstacle_color
    }
    obstacles.append(obstacle)

def update_obstacles():
    for obstacle in obstacles[:]: 
        obstacle["rect"].x -= 5
        pygame.draw.rect(screen, obstacle["color"], obstacle["rect"]) 
        

        if obstacle["rect"].right < 0:
            obstacles.remove(obstacle)

def check_for_collision():
    for obstacle in obstacles:
        if player.colliderect(obstacle["rect"]):
            return True


def check_for_game_over():
    if check_for_collision():
        return True
    return False

