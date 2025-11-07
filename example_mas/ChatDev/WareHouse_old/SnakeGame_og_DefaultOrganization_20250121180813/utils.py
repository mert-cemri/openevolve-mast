'''
Utility functions for drawing.
'''
import pygame
def draw_grid(surface, screen_width, screen_height, grid_size):
    for x in range(0, screen_width, grid_size):
        pygame.draw.line(surface, (40, 40, 40), (x, 0), (x, screen_height))
    for y in range(0, screen_height, grid_size):
        pygame.draw.line(surface, (40, 40, 40), (0, y), (screen_width, y))