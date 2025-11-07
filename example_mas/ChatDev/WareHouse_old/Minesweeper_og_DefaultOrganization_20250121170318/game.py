'''
Contains the MinesweeperGame class which handles the game logic.
'''
import random
class MinesweeperGame:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.uncovered_positions = set()
        self.initialize_board()
    def initialize_board(self):
        # Place mines randomly
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mine_positions.add((r, c))
        # Calculate adjacent mine counts
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in self.mine_positions:
                    self.board[r][c] = str(self.count_adjacent_mines(r, c))
    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if (nr, nc) in self.mine_positions:
                        count += 1
        return count
    def uncover_cell(self, row, col):
        if (row, col) in self.mine_positions:
            return False  # Game over
        # If the cell is already uncovered, return True
        if (row, col) in self.uncovered_positions:
            return True
        # Update the board to show the uncovered cell
        self.uncovered_positions.add((row, col))
        adjacent_mines = self.count_adjacent_mines(row, col)
        self.board[row][col] = str(adjacent_mines)
        # If no adjacent mines, recursively uncover adjacent cells
        if adjacent_mines == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.uncover_cell(nr, nc)
        return True
    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and (row, col) not in self.uncovered_positions
    def get_board(self):
        return self.board