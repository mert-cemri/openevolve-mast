'''
Board class represents the game board and handles drawing the game state.
'''
import pygame
class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.cell_size = 20
    def draw(self, snake, food):
        self.screen.fill((0, 0, 0))  # Clear the screen with black
        for x, y in snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        fx, fy = food.position
        pygame.draw.rect(self.screen, (255, 0, 0), (fx * self.cell_size, fy * self.cell_size, self.cell_size, self.cell_size))
        pygame.display.set_caption(f"Snake Game - Score: {len(snake.body) - 3}")