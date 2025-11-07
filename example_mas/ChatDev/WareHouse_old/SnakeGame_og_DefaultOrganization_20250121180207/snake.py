'''
Snake class represents the snake in the game.
'''
import pygame
from utils import random_position
class Snake:
    def __init__(self):
        self.body = [random_position()]
        self.direction = pygame.K_RIGHT
    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = key
        elif key == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = key
        elif key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = key
        elif key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = key
    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_UP:
            head_y -= 10
        elif self.direction == pygame.K_DOWN:
            head_y += 10
        elif self.direction == pygame.K_LEFT:
            head_x -= 10
        elif self.direction == pygame.K_RIGHT:
            head_x += 10
        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        self.body.pop()
    def grow(self):
        self.body.append(self.body[-1])
    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or not (0 <= head[0] < 600 and 0 <= head[1] < 400)
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))