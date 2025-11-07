'''
Defines the Board class representing the game board and its operations.
'''
from candy import Candy
class Board:
    def __init__(self, size=8):
        self.size = size
        self.grid = []
        self.score = 0
        self.initialize_board()
    def initialize_board(self):
        self.grid = [[Candy() for _ in range(self.size)] for _ in range(self.size)]
    def swap_candies(self, x1, y1, x2, y2):
        self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]
    def find_matches(self):
        matches = []
        # Check rows for matches
        for x in range(self.size):
            y = 0
            while y < self.size - 2:
                match_length = 1
                while y + match_length < self.size and self.grid[x][y].type == self.grid[x][y + match_length].type:
                    match_length += 1
                if match_length >= 3:
                    matches.append([(x, y + i) for i in range(match_length)])
                y += match_length
        # Check columns for matches
        for y in range(self.size):
            x = 0
            while x < self.size - 2:
                match_length = 1
                while x + match_length < self.size and self.grid[x][y].type == self.grid[x + match_length][y].type:
                    match_length += 1
                if match_length >= 3:
                    matches.append([(x + i, y) for i in range(match_length)])
                x += match_length
        return matches
    def clear_matches(self, matches):
        for match in matches:
            for x, y in match:
                self.grid[x][y] = None
                self.score += 10 * len(match)  # Award more points for longer matches
    def drop_candies(self):
        for y in range(self.size):
            empty_slots = 0
            for x in range(self.size-1, -1, -1):
                if self.grid[x][y] is None:
                    empty_slots += 1
                elif empty_slots > 0:
                    self.grid[x+empty_slots][y] = self.grid[x][y]
                    self.grid[x][y] = None
    def refill_board(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] is None:
                    self.grid[x][y] = Candy()
    def update_board(self):
        matches = self.find_matches()
        while matches:
            self.clear_matches(matches)
            self.drop_candies()
            self.refill_board()
            matches = self.find_matches()