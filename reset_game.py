from player_settings import player, player_x, player_y
from obstacles import reset_obstacles, spawn_obstacle
from screen import SCREEN_WIDTH
import pygame
import random

pygame.init()

# Set all game variables to 0
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
