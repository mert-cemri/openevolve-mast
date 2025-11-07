'''
Handles the game logic for Minesweeper, including board setup, mine placement, and game state updates.
'''
import random
class MinesweeperGame:
    def __init__(self, size=9, mines=10):
        self.size = size
        self.mines = mines
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.place_mines()
        self.calculate_adjacent_mines()
    def place_mines(self):
        placed_mines = 0
        while placed_mines < self.mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.board[row][col] != 'M':
                self.board[row][col] = 'M'
                placed_mines += 1
    def calculate_adjacent_mines(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 'M':
                    continue
                count = 0
                for r in range(max(0, row-1), min(self.size, row+2)):
                    for c in range(max(0, col-1), min(self.size, col+2)):
                        if self.board[r][c] == 'M':
                            count += 1
                self.board[row][col] = count
    def uncover_cell(self, row, col):
        if self.revealed[row][col]:
            return False
        self.revealed[row][col] = True
        if self.board[row][col] == 'M':
            return True
        if self.board[row][col] == 0:
            for r in range(max(0, row-1), min(self.size, row+2)):
                for c in range(max(0, col-1), min(self.size, col+2)):
                    if not self.revealed[r][c]:
                        self.uncover_cell(r, c)
        return False
    def check_win(self):
        for row in range(self.size):
            for col in range(self.size):
                if not self.revealed[row][col] and self.board[row][col] != 'M':
                    return False
        return True