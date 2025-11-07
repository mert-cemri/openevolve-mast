'''
Contains the TetrisGame class that manages the game logic.
'''
import pygame
import random
from tetromino import Tetromino
class TetrisGame:
    WIDTH = 10
    HEIGHT = 20
    CELL_SIZE = 30
    COLORS = [
        (0, 255, 255),  # I
        (0, 0, 255),    # J
        (255, 165, 0),  # L
        (255, 255, 0),  # O
        (0, 255, 0),    # S
        (128, 0, 128),  # T
        (255, 0, 0)     # Z
    ]
    SHAPES = [
        [[1, 3, 5, 7]],  # I
        [[2, 4, 5, 7]],  # Z
        [[3, 5, 4, 6]],  # S
        [[3, 5, 4, 7]],  # T
        [[2, 3, 5, 7]],  # L
        [[3, 5, 7, 6]],  # J
        [[2, 3, 4, 5]]   # O
    ]
    def __init__(self):
        self.board = [[0] * self.WIDTH for _ in range(self.HEIGHT)]
        self.score = 0
        self.speed = 500
        self.current_tetromino = None
        self.spawn_tetromino()
    def spawn_tetromino(self):
        shape_idx = random.randint(0, len(self.SHAPES) - 1)
        self.current_tetromino = Tetromino(self.SHAPES[shape_idx], self.COLORS[shape_idx])
        self.current_tetromino.x = self.WIDTH // 2 - 2
        self.current_tetromino.y = 0
    def move(self, dx, dy):
        if self.valid_move(self.current_tetromino, dx, dy):
            self.current_tetromino.x += dx
            self.current_tetromino.y += dy
            return True
        return False
    def rotate(self):
        original_rotation = self.current_tetromino.rotation
        self.current_tetromino.rotate()
        if not self.valid_move(self.current_tetromino, 0, 0):
            self.current_tetromino.rotation = original_rotation
    def drop(self):
        while self.move(0, 1):
            continue
        self.lock_tetromino()
    def lock_tetromino(self):
        for x, y in self.current_tetromino.get_cells():
            if y >= 0:
                self.board[y][x] = self.current_tetromino.color
    def clear_lines(self):
        lines_cleared = 0
        for i in range(len(self.board)-1, -1, -1):
            if 0 not in self.board[i]:
                del self.board[i]
                self.board.insert(0, [0]*self.WIDTH)
                lines_cleared += 1
        self.score += lines_cleared ** 2 * 100
        self.update_speed()
    def update_speed(self):
        self.speed = max(100, 500 - (self.score // 500) * 50)
    def valid_move(self, tetromino, dx, dy):
        for x, y in tetromino.get_cells(dx, dy):
            if x < 0 or x >= self.WIDTH or y >= self.HEIGHT or (y >= 0 and self.board[y][x]):
                return False
        return True
    def is_game_over(self):
        return any(self.board[0])
    def draw(self, screen):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if self.board[y][x]:
                    pygame.draw.rect(screen, self.board[y][x],
                                     (x*self.CELL_SIZE, y*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        for x, y in self.current_tetromino.get_cells():
            if y >= 0:
                pygame.draw.rect(screen, self.current_tetromino.color,
                                 (x*self.CELL_SIZE, y*self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))