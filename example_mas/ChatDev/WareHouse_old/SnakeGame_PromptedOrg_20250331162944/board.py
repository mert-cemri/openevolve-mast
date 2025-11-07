'''
Board class to represent the game board.
'''
import pygame
class Board:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.cell_size = 20
        self.screen = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))
    def draw(self, snake, food):
        self.screen.fill((0, 0, 0))
        for segment in snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (segment[0] * self.cell_size, segment[1] * self.cell_size, self.cell_size, self.cell_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (food.position[0] * self.cell_size, food.position[1] * self.cell_size, self.cell_size, self.cell_size))