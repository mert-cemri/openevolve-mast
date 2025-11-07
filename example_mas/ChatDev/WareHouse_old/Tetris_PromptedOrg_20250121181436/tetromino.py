'''
Represents a tetromino, including its shape, position, and rotation.
'''
import random
class Tetromino:
    SHAPES = [
        [[1, 1, 1, 1]],  # I
        [[1, 1, 1], [0, 1, 0]],  # T
        [[1, 1, 0], [0, 1, 1]],  # Z
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 1], [1, 1]],  # O
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 1, 1], [0, 0, 1]]   # J
    ]
    def __init__(self):
        self.shape = random.choice(self.SHAPES)
        self.x = 3
        self.y = 0
    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
    def move(self, dx, dy, board):
        # Attempt to move
        self.x += dx
        self.y += dy
        # Check for collision
        if board.is_collision(self):
            # Revert move if collision detected
            self.x -= dx
            self.y -= dy
    def get_blocks(self):
        return [(self.x + x, self.y + y) for y, row in enumerate(self.shape) for x, cell in enumerate(row) if cell]