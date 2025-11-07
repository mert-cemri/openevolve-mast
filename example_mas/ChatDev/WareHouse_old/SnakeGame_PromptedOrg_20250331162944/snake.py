'''
Snake class to represent the snake's position and movement.
'''
import pygame
from collections import deque
class Snake:
    def __init__(self, board_width, board_height):
        self.body = deque([(board_width // 2, board_height // 2)])
        self.direction = pygame.K_RIGHT
        self.growing = False
        self.board_width = board_width
        self.board_height = board_height
    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == pygame.K_UP:
            head_y -= 1
        elif self.direction == pygame.K_DOWN:
            head_y += 1
        elif self.direction == pygame.K_LEFT:
            head_x -= 1
        elif self.direction == pygame.K_RIGHT:
            head_x += 1
        new_head = (head_x, head_y)
        self.body.appendleft(new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
    def grow(self):
        self.growing = True
    def change_direction(self, key):
        # Prevent the snake from reversing direction
        opposite_directions = {
            pygame.K_UP: pygame.K_DOWN,
            pygame.K_DOWN: pygame.K_UP,
            pygame.K_LEFT: pygame.K_RIGHT,
            pygame.K_RIGHT: pygame.K_LEFT
        }
        if key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] and key != opposite_directions[self.direction]:
            self.direction = key
    def check_collision(self):
        head = self.body[0]
        # Check if the head is within the snake's body
        if head in list(self.body)[1:]:
            return True
        # Check if the head is out of the board boundaries
        if head[0] < 0 or head[0] >= self.board_width or head[1] < 0 or head[1] >= self.board_height:
            return True
        return False