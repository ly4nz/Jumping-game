from player_settings import player, player_x, player_y
from obstacles import obstacle_colors, obstacles, reset_obstacles
from screen import SCREEN_WIDTH
import pygame
import random
pygame.init()

def reset_game():
    player.x = player_x
    player.y = player_y
    velocity = 0
    jumping = False
    on_ground = True
    global scroll
    scroll = 0
    reset_obstacles()
    spawn_obstacle()

def spawn_obstacle():
    obstacle_color = random.choice(obstacle_colors)
    obstacle_y = 400
    obstacle = {
        "rect": pygame.Rect(SCREEN_WIDTH, obstacle_y, 25, 25),
        "color": obstacle_color
    }
    obstacles.append(obstacle)