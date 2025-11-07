'''
Board class represents the Tetris board, handles the placement of tetrominoes, and clears completed lines.
'''
class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
    def can_place(self, tetromino):
        # Check if tetromino can be placed on the board
        for x, y in tetromino.get_coordinates():
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            if self.grid[y][x] != 0:
                return False
        return True
    def place(self, tetromino):
        # Place tetromino on the board
        for x, y in tetromino.get_coordinates():
            self.grid[y][x] = 1
    def clear_lines(self):
        # Clear completed lines and shift down
        self.grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        while len(self.grid) < self.height:
            self.grid.insert(0, [0] * self.width)
    def display(self, stdscr):
        # Display the board
        for y, row in enumerate(self.grid):
            stdscr.addstr(y, 0, ''.join(['#' if cell else '.' for cell in row]))