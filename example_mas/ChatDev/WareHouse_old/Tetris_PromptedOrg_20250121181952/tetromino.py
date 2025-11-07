'''
Tetromino class represents the tetrominoes, handles their shapes, rotations, and movements.
'''
import random
class Tetromino:
    SHAPES = [
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # O shape
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # I shape
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # L shape
        [(0, 1), (1, 1), (2, 1), (2, 0)],  # J shape
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # S shape
        [(0, 1), (1, 1), (1, 0), (2, 0)],  # Z shape
        [(0, 0), (1, 0), (1, 1), (2, 0)],  # T shape
    ]
    def __init__(self, board):
        self.shape = random.choice(Tetromino.SHAPES)
        self.x = 3
        self.y = 0
        self.board = board
    def get_coordinates(self):
        return [(x + self.x, y + self.y) for x, y in self.shape]
    def move_down(self):
        self.y += 1
    def move_up(self):
        self.y -= 1
    def move_left(self):
        self.x -= 1
    def move_right(self):
        self.x += 1
    def rotate(self):
        original_shape = self.shape
        self.shape = [(y, -x) for x, y in self.shape]
        if not self.board.can_place(self):
            # Attempt to kickback
            self.x += 1
            if not self.board.can_place(self):
                self.x -= 2
                if not self.board.can_place(self):
                    self.x += 1
                    self.y += 1
                    if not self.board.can_place(self):
                        self.y -= 2
                        if not self.board.can_place(self):
                            # Revert rotation if all kickbacks fail
                            self.shape = original_shape
                            self.y += 1