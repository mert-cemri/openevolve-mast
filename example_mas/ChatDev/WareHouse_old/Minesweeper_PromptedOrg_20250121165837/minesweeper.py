'''
This module contains the MinesweeperGame class which manages the game state, including the board, mines, and user interactions.
'''
import random
class MinesweeperGame:
    def __init__(self, size=9, mines=10):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.mine_locations = set()
        self.uncovered = set()
        self.place_mines()
        self.calculate_adjacent_mines()
    def place_mines(self):
        while len(self.mine_locations) < self.mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if (row, col) not in self.mine_locations:
                self.mine_locations.add((row, col))
                self.board[row][col] = 'M'
    def calculate_adjacent_mines(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 'M':
                    continue
                mine_count = 0
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == 'M':
                        mine_count += 1
                self.board[row][col] = str(mine_count) if mine_count > 0 else ' '
    def uncover_cell(self, row, col):
        if (row, col) in self.uncovered:
            return
        self.uncovered.add((row, col))
        if self.board[row][col] == 'M':
            raise ValueError("Mine hit! Game over.")
        if self.board[row][col] == ' ':
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < self.size and 0 <= c < self.size and (r, c) not in self.uncovered:
                    self.uncover_cell(r, c)
    def display_board(self):
        for row in range(self.size):
            display_row = []
            for col in range(self.size):
                if (row, col) in self.uncovered:
                    display_row.append(self.board[row][col] if self.board[row][col] != ' ' else '0')
                else:
                    display_row.append('X')  # Use 'X' to represent covered cells
            print(' '.join(display_row))
        print()
    def check_win(self):
        return len(self.uncovered) == self.size * self.size - self.mines