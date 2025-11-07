'''
Handles the game board for Reversi (Othello), including state management and move validation.
'''
class Board:
    def __init__(self):
        # Initialize an 8x8 board with starting positions
        self.size = 8
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.grid[3][3] = self.grid[4][4] = 'W'
        self.grid[3][4] = self.grid[4][3] = 'B'
    def is_valid_move(self, row, col, color):
        # Check if a move is valid
        if self.grid[row][col] != ' ':
            return False
        # Check all directions for valid flips
        return any(self._check_direction(row, col, color, dr, dc) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)])
    def _check_direction(self, row, col, color, dr, dc):
        # Check a specific direction for valid flips
        opponent = 'B' if color == 'W' else 'W'
        r, c = row + dr, col + dc
        if not (0 <= r < self.size and 0 <= c < self.size) or self.grid[r][c] != opponent:
            return False
        while 0 <= r < self.size and 0 <= c < self.size:
            if self.grid[r][c] == ' ':
                return False
            if self.grid[r][c] == color:
                return True
            r += dr
            c += dc
        return False
    def place_disc(self, row, col, color):
        # Place a disc on the board and flip opponent discs
        if not self.is_valid_move(row, col, color):
            return False
        self.grid[row][col] = color
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            if self._check_direction(row, col, color, dr, dc):
                self._flip_discs(row, col, color, dr, dc)
        return True
    def _flip_discs(self, row, col, color, dr, dc):
        # Flip opponent discs in a specific direction
        opponent = 'B' if color == 'W' else 'W'
        r, c = row + dr, col + dc
        while self.grid[r][c] == opponent:
            self.grid[r][c] = color
            r += dr
            c += dc
    def is_full(self):
        # Check if the board is full
        return all(self.grid[row][col] != ' ' for row in range(self.size) for col in range(self.size))
    def print_board(self):
        # Print the current board state
        for row in self.grid:
            print(' '.join(row))
        print()