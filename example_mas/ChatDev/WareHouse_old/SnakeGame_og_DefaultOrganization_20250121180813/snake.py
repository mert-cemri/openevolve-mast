'''
Snake class to manage snake behavior.
'''
import pygame
import random
class Snake:
    def __init__(self):
        self.positions = [(100, 100)]
        self.direction = 'RIGHT'
        self.color = (0, 255, 0)
    def change_direction(self, direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != opposite_directions[self.direction] and direction != self.direction:
            self.direction = direction
    def move(self):
        x, y = self.positions[0]
        if self.direction == 'UP':
            y -= 20
        elif self.direction == 'DOWN':
            y += 20
        elif self.direction == 'LEFT':
            x -= 20
        elif self.direction == 'RIGHT':
            x += 20
        new_head = (x, y)
        self.positions = [new_head] + self.positions[:-1]
    def grow(self):
        self.positions.append(self.positions[-1])
    def check_collision(self, screen_width, screen_height):
        x, y = self.positions[0]
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            return True
        if len(self.positions) != len(set(self.positions)):
            return True
        return False
    def draw(self, surface, grid_size):
        for position in self.positions:
            rect = pygame.Rect(position[0], position[1], grid_size, grid_size)
            pygame.draw.rect(surface, self.color, rect)