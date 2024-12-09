import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
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

def update_obstacles(screen):
    for obstacle in obstacles[:]:
        obstacle["rect"].x -= 5
        pygame.draw.rect(screen, obstacle["color"], obstacle["rect"])
        
        if obstacle["rect"].right < 0:
            obstacles.remove(obstacle)
