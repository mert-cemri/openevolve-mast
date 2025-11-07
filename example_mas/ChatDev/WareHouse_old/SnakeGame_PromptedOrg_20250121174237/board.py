'''
Board module to render the game state.
'''
import pygame
class Board:
    def __init__(self, screen, snake, food, width, height, block_size):
        self.screen = screen
        self.snake = snake
        self.food = food
        self.width = width
        self.height = height
        self.block_size = block_size
    def draw(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], self.block_size, self.block_size))
        pygame.display.flip()