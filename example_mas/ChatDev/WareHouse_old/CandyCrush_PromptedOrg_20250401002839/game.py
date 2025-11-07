'''
Core game logic for Candy Crush-like match-3 puzzle game with move-based constraints.
'''
import random
from enum import Enum
class Candy(Enum):
    RED = '🔴'
    GREEN = '🟢'
    BLUE = '🔵'
    YELLOW = '🟡'
    PURPLE = '🟣'
class CandyCrushGame:
    def __init__(self, rows=8, cols=8, max_moves=30):
        self.rows = rows
        self.cols = cols
        self.max_moves = max_moves
        self.board = [[random.choice(list(Candy)) for _ in range(cols)] for _ in range(rows)]
        self.score = 0
        self.moves = 0
        self.remove_initial_matches()
    def remove_initial_matches(self):
        matches = self.find_matches()
        while matches:
            self.clear_matches(matches)
            self.drop_candies()
            self.fill_board()
            matches = self.find_matches()
    def swap_candies(self, pos1, pos2):
        if not self.is_valid_swap(pos1, pos2):
            return False
        r1, c1 = pos1
        r2, c2 = pos2
        if not (0 <= r1 < self.rows and 0 <= c1 < self.cols and 0 <= r2 < self.rows and 0 <= c2 < self.cols):
            return False
        self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
        matches = self.find_matches()
        if matches:
            self.moves += 1
            while matches:
                self.clear_matches(matches)
                self.drop_candies()
                self.fill_board()
                matches = self.find_matches()
            return True
        else:
            self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
            return False
    def find_matches(self):
        matches = set()
        # Check horizontal matches
        for r in range(self.rows):
            count = 1
            for c in range(1, self.cols):
                if self.board[r][c] == self.board[r][c-1]:
                    count += 1
                else:
                    if count >= 3:
                        matches.update((r, c-i-1) for i in range(count))
                    count = 1
            if count >= 3:
                matches.update((r, self.cols-i-1) for i in range(count))
        # Check vertical matches
        for c in range(self.cols):
            count = 1
            for r in range(1, self.rows):
                if self.board[r][c] == self.board[r-1][c]:
                    count += 1
                else:
                    if count >= 3:
                        matches.update((r-i-1, c) for i in range(count))
                    count = 1
            if count >= 3:
                matches.update((self.rows-i-1, c) for i in range(count))
        return matches
    def clear_matches(self, matches):
        for r, c in matches:
            self.board[r][c] = None
        self.score += len(matches) * 10
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
                    self.board[r][c] = random.choice(list(Candy))
    def is_valid_swap(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            return False
        return 0 <= r1 < self.rows and 0 <= c1 < self.cols and 0 <= r2 < self.rows and 0 <= c2 < self.cols
    def has_possible_moves(self):
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in [(0,1),(1,0)]:
                    nr, nc = r+dr, c+dc
                    if nr < self.rows and nc < self.cols:
                        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
                        if self.find_matches():
                            self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
                            return True
                        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
        return False
    def print_board(self):
        for row in self.board:
            print(' '.join(candy.value for candy in row))
        print(f"Score: {self.score} | Moves: {self.moves}/{self.max_moves}")