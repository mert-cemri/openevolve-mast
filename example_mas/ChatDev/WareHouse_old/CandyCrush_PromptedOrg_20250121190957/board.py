'''
This module defines the Board class, which represents the game board and contains methods for managing the board state.
'''
import random
from candy import Candy
class Board:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.grid = [[Candy(random.choice(['red', 'green', 'blue', 'yellow', 'purple'])) for _ in range(cols)] for _ in range(rows)]
        self.score = 0
    def swap_candies(self, x1, y1, x2, y2):
        self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]
    def find_matches(self):
        matches = set()
        # Check for horizontal matches
        for row in range(self.rows):
            for col in range(self.cols - 2):
                if self.grid[row][col].type == self.grid[row][col + 1].type == self.grid[row][col + 2].type:
                    matches.update({(row, col), (row, col + 1), (row, col + 2)})
        # Check for vertical matches
        for col in range(self.cols):
            for row in range(self.rows - 2):
                if self.grid[row][col].type == self.grid[row + 1][col].type == self.grid[row + 2][col].type:
                    matches.update({(row, col), (row + 1, col), (row + 2, col)})
        return list(matches)
    def clear_matches(self, matches):
        for (row, col) in matches:
            self.grid[row][col] = None
        self.score += len(matches)
    def drop_candies(self):
        for col in range(self.cols):
            empty_row = self.rows - 1
            for row in range(self.rows - 1, -1, -1):
                if self.grid[row][col] is not None:
                    self.grid[empty_row][col] = self.grid[row][col]
                    empty_row -= 1
            for row in range(empty_row, -1, -1):
                self.grid[row][col] = None
    def fill_empty_spaces(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] is None:
                    self.grid[row][col] = Candy(random.choice(['red', 'green', 'blue', 'yellow', 'purple']))
    def update_board(self):
        matches = self.find_matches()
        while matches:
            self.clear_matches(matches)
            self.drop_candies()
            self.fill_empty_spaces()
            matches = self.find_matches()