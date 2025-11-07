'''
Board class represents the game board and handles operations related to it.
'''
import random
import pygame
from candy import Candy
class Board:
    def __init__(self, score, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.grid = self.initialize_board()
        self.score = score
    def initialize_board(self):
        return [[Candy(random.choice(['red', 'green', 'blue', 'yellow', 'purple'])) for _ in range(self.cols)] for _ in range(self.rows)]
    def swap_candies(self, pos1, pos2):
        self.grid[pos1[0]][pos1[1]], self.grid[pos2[0]][pos2[1]] = self.grid[pos2[0]][pos2[1]], self.grid[pos1[0]][pos1[1]]
        if not self.find_matches():
            self.grid[pos1[0]][pos1[1]], self.grid[pos2[0]][pos2[1]] = self.grid[pos2[0]][pos2[1]], self.grid[pos1[0]][pos1[1]]
    def find_matches(self):
        matches = []
        # Check horizontal matches
        for row in range(self.rows):
            for col in range(self.cols - 2):
                if self.grid[row][col].color == self.grid[row][col + 1].color == self.grid[row][col + 2].color:
                    matches.append((row, col))
                    matches.append((row, col + 1))
                    matches.append((row, col + 2))
        # Check vertical matches
        for col in range(self.cols):
            for row in range(self.rows - 2):
                if self.grid[row][col].color == self.grid[row + 1][col].color == self.grid[row + 2][col].color:
                    matches.append((row, col))
                    matches.append((row + 1, col))
                    matches.append((row + 2, col))
        return list(set(matches))
    def remove_matches(self, matches):
        for row, col in matches:
            self.grid[row][col] = None
    def drop_candies(self):
        for col in range(self.cols):
            for row in range(self.rows - 1, -1, -1):
                if self.grid[row][col] is None:
                    for above_row in range(row - 1, -1, -1):
                        if self.grid[above_row][col] is not None:
                            self.grid[row][col] = self.grid[above_row][col]
                            self.grid[above_row][col] = None
                            break
    def fill_empty_spaces(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] is None:
                    self.grid[row][col] = Candy(random.choice(['red', 'green', 'blue', 'yellow', 'purple']))
    def update(self):
        while True:
            matches = self.find_matches()
            if not matches:
                break
            self.score.add_points(len(matches))  # Update score
            self.remove_matches(matches)
            self.drop_candies()
            self.fill_empty_spaces()
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] is not None:
                    self.grid[row][col].draw(screen, col * 50, row * 50)