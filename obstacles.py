import pygame
import random
from screen import SCREEN_WIDTH
from player_settings import player

pygame.init()

# List of possible obstacle colors
obstacle_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# List to hold all obstacles
obstacles = []

# Clear the list obstacles
def reset_obstacles():
    global obstacles
    obstacles.clear()

# Spawn a new obstacle at the right side of the screen
def spawn_obstacle():

    # Choose a random color for the obstacle
    obstacle_color = random.choice(obstacle_colors)
    
    # Set obstacle x and y
    obstacle_y = 400  
        
    # Create a new obstacle at the right edge of the screen
    obstacle = {
        "rect": pygame.Rect(SCREEN_WIDTH, obstacle_y, 25, 25),  # x, y, width, height
        "color": obstacle_color
    }
    
    # Add the obstacle to the list
    obstacles.append(obstacle)

# Update all obstacles: move them left and check if they go off-screen
def update_obstacles(screen):
    
    for obstacle in obstacles[:]:
        # Move obstacles to the left
        obstacle["rect"].x -= 5  # You can change the speed here
        
        # Draw the obstacle on the screen
        pygame.draw.rect(screen, obstacle["color"], obstacle["rect"])
        
        # Remove obstacles that have gone off the screen
        if obstacle["rect"].right < 0:
            obstacles.remove(obstacle)

# Check if player has collided with an obstacle
def check_for_collision():
    for obstacle in obstacles:
        if player.colliderect(obstacle["rect"]):
            print("Collided!")
            return True
    return False



