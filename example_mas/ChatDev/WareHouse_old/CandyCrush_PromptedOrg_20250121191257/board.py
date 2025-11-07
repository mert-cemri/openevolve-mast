'''
This module contains the GameBoard class which represents the game board for the match-3 puzzle game.
'''
import random
from candy import Candy
class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[Candy.random_candy() for _ in range(cols)] for _ in range(rows)]
    def swap(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        if abs(r1 - r2) + abs(c1 - c2) == 1:  # Ensure they are adjacent
            # Perform the swap
            self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
            # Check for matches
            if self.find_matches():
                return True
            else:
                # Revert the swap if no matches are found
                self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
        return False
    def find_matches(self):
        matches = []
        # Check rows for matches
        for r in range(self.rows):
            match = []
            for c in range(self.cols):
                if c == 0 or self.board[r][c].color != self.board[r][c-1].color:
                    if len(match) >= 3:
                        matches.append(match)
                    match = [(r, c)]
                else:
                    match.append((r, c))
            if len(match) >= 3:
                matches.append(match)
        # Check columns for matches
        for c in range(self.cols):
            match = []
            for r in range(self.rows):
                if r == 0 or self.board[r][c].color != self.board[r-1][c].color:
                    if len(match) >= 3:
                        matches.append(match)
                    match = [(r, c)]
                else:
                    match.append((r, c))
            if len(match) >= 3:
                matches.append(match)
        return matches
    def clear_matches(self, matches):
        for match in matches:
            for r, c in match:
                self.board[r][c] = None
    def drop_candies(self):
        for c in range(self.cols):
            empty_row = self.rows - 1
            for r in range(self.rows - 1, -1, -1):
                if self.board[r][c] is not None:
                    self.board[empty_row][c] = self.board[r][c]
                    empty_row -= 1
            for r in range(empty_row, -1, -1):
                self.board[r][c] = None
    def fill_board(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] is None:
                    self.board[r][c] = Candy.random_candy()
    def print_board(self):
        for row in self.board:
            print(' '.join(candy.color for candy in row))