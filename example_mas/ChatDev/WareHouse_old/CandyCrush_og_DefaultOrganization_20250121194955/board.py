'''
Board class that manages the game board and candies.
'''
import random
from candy import Candy
class Board:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.grid = [[Candy(random.randint(0, 5), (row, col)) for col in range(cols)] for row in range(rows)]
        self.matches = []
    def swap_candies(self, pos1, pos2):
        if self.check_adjacent(pos1, pos2):
            self.grid[pos1[0]][pos1[1]], self.grid[pos2[0]][pos2[1]] = self.grid[pos2[0]][pos2[1]], self.grid[pos1[0]][pos1[1]]
            if not self.find_matches():
                # Swap back if no match is found
                self.grid[pos1[0]][pos1[1]], self.grid[pos2[0]][pos2[1]] = self.grid[pos2[0]][pos2[1]], self.grid[pos1[0]][pos1[1]]
    def find_matches(self):
        self.matches.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                # Check for horizontal matches
                match_length = 1
                while col + match_length < self.cols and self.grid[row][col].type == self.grid[row][col + match_length].type:
                    match_length += 1
                if match_length >= 3:
                    for i in range(match_length):
                        self.matches.append((row, col + i))
                # Check for vertical matches
                match_length = 1
                while row + match_length < self.rows and self.grid[row][col].type == self.grid[row + match_length][col].type:
                    match_length += 1
                if match_length >= 3:
                    for i in range(match_length):
                        self.matches.append((row + i, col))
        return len(self.matches) > 0
    def clear_matches(self, score):
        for (row, col) in self.matches:
            self.grid[row][col] = None
            score.add_points(10)  # Add points for each candy cleared
    def drop_candies(self):
        for col in range(self.cols):
            empty_spots = 0
            for row in range(self.rows - 1, -1, -1):
                if self.grid[row][col] is None:
                    empty_spots += 1
                elif empty_spots > 0:
                    self.grid[row + empty_spots][col] = self.grid[row][col]
                    self.grid[row][col] = None
    def refill_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] is None:
                    self.grid[row][col] = Candy(random.randint(0, 5), (row, col))
    def update(self, score):
        if self.find_matches():
            self.clear_matches(score)
            self.drop_candies()
            self.refill_board()
    def draw(self, screen, images):
        for row in range(self.rows):
            for col in range(self.cols):
                candy = self.grid[row][col]
                if candy:
                    screen.blit(images[candy.type], (col * 50, row * 50))
    def check_adjacent(self, pos1, pos2):
        return (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or (abs(pos1[1] - pos2[1]) == 1 and pos1[0] == pos2[0])