import pygame
import random
from game_data import SCREEN_WIDTH
from player_settings import player

pygame.init()

# List of possible obstacle colors
obstacle_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# List to hold all obstacles
obstacles = []

def reset_obstacles():
    """Clear the list of obstacles."""
    global obstacles
    obstacles.clear()

def spawn_obstacle():
    """Spawn a new obstacle at the right side of the screen."""
    # Choose a random color for the obstacle
    obstacle_color = random.choice(obstacle_colors)
    
    # Fixed obstacle height (for example)
    obstacle_y = 400  # You can adjust this value for varying obstacle heights
    
    # Randomly set the obstacle width, making it variable
    obstacle_width = random.randint(20, 50)
    
    # Create a new obstacle at the right edge of the screen
    obstacle = {
        "rect": pygame.Rect(SCREEN_WIDTH, obstacle_y, obstacle_width, 25),  # x, y, width, height
        "color": obstacle_color
    }
    
    # Add the obstacle to the list
    obstacles.append(obstacle)

def update_obstacles(screen):
    """Update all obstacles: move them left and check if they go off-screen."""
    for obstacle in obstacles[:]:
        # Move obstacles to the left
        obstacle["rect"].x -= 5  # You can change the speed here
        
        # Draw the obstacle on the screen
        pygame.draw.rect(screen, obstacle["color"], obstacle["rect"])
        
        # Remove obstacles that have gone off the screen (off the left side)
        if obstacle["rect"].right < 0:
            obstacles.remove(obstacle)

def check_for_collision():
    """Check if the player collides with any obstacle."""
    for obstacle in obstacles:
        if player.colliderect(obstacle["rect"]):
            return True
    return False

def check_for_game_over():
    """Return True if the player collides with an obstacle (Game Over)."""
    return check_for_collision()

