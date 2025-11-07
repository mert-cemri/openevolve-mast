'''
This module contains the Game class which handles the core logic of the 2048 game.
'''
import random
from grid import Grid
import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
class Game:
    def __init__(self, size=10):
        self.size = size
        self.grid = Grid(size)
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()
        pygame.init()
        self.tile_size = 60  # Adjusted tile size
        self.screen = pygame.display.set_mode((self.tile_size * size, self.tile_size * size))
        pygame.display.set_caption('2048 Game')
    def add_new_tile(self):
        empty_positions = self.grid.get_empty_positions()
        if not empty_positions:
            return
        x, y = random.choice(empty_positions)
        self.grid.set_tile(x, y, 2 if random.random() < 0.9 else 4)
    def move(self, direction):
        if direction in ['up', 'down', 'left', 'right']:
            moved, score = self.grid.move(direction)
            if moved:
                self.score += score
                self.add_new_tile()
                return True
        return False
    def is_game_over(self):
        return not self.grid.can_move()
    def get_score(self):
        return self.score
    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.move('up')
                    elif event.key == K_DOWN:
                        self.move('down')
                    elif event.key == K_LEFT:
                        self.move('left')
                    elif event.key == K_RIGHT:
                        self.move('right')
            self.render()
            pygame.display.update()
            if self.is_game_over():
                print("Game Over!")
                running = False
    def render(self):
        self.screen.fill((187, 173, 160))
        for row in range(self.size):
            for col in range(self.size):
                value = self.grid.grid[row][col]
                pygame.draw.rect(self.screen, (205, 193, 180), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                if value != 0:
                    font = pygame.font.Font(None, 48)  # Adjusted font size
                    text = font.render(str(value), True, (119, 110, 101))
                    text_rect = text.get_rect(center=(col * self.tile_size + self.tile_size // 2, row * self.tile_size + self.tile_size // 2))
                    self.screen.blit(text, text_rect)