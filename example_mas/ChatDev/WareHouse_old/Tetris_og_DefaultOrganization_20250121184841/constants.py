'''
Constants for the Tetris game, including screen dimensions, colors, and tetromino shapes.
'''
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLOCK_SIZE = 30
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TETROMINO_SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]