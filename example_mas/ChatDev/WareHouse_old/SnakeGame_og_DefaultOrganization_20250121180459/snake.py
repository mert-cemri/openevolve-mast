'''
Defines the Snake class, which represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = 'RIGHT'
        self.growing = False
    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - 10)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 10)
        elif self.direction == 'LEFT':
            new_head = (head_x - 10, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 10, head_y)
        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
    def grow(self):
        self.growing = True
    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or head[0] < 0 or head[0] >= 600 or head[1] < 0 or head[1] >= 400
    def head_position(self):
        return self.body[0]
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))