'''
Board management and logic for the match-3 game.
'''
import random
import pygame
from candy import Candy
class Board:
    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols
        self.grid = []
        self.cleared_matches = []
        self.selected_candy = None
        self.initialize_board()
    def initialize_board(self):
        self.grid = [[Candy(random.randint(1, 5)) for _ in range(self.cols)] for _ in range(self.rows)]
    def swap_candies(self, pos1, pos2):
        self.grid[pos1[0]][pos1[1]], self.grid[pos2[0]][pos2[1]] = self.grid[pos2[0]][pos2[1]], self.grid[pos1[0]][pos1[1]]
    def check_matches(self):
        matches = []
        # Check horizontal matches
        for row in range(self.rows):
            for col in range(self.cols - 2):
                if self.grid[row][col].candy_type == self.grid[row][col + 1].candy_type == self.grid[row][col + 2].candy_type:
                    matches.append((row, col))
                    matches.append((row, col + 1))
                    matches.append((row, col + 2))
        # Check vertical matches
        for col in range(self.cols):
            for row in range(self.rows - 2):
                if self.grid[row][col].candy_type == self.grid[row + 1][col].candy_type == self.grid[row + 2][col].candy_type:
                    matches.append((row, col))
                    matches.append((row + 1, col))
                    matches.append((row + 2, col))
        return matches
    def clear_matches(self):
        matches = self.check_matches()
        self.cleared_matches = matches
        for (row, col) in matches:
            self.grid[row][col] = None
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
                    self.grid[row][col] = Candy(random.randint(1, 5))
    def update(self):
        while True:
            self.clear_matches()
            if not self.cleared_matches:
                break
            self.drop_candies()
            self.refill_board()
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                candy = self.grid[row][col]
                if candy:
                    candy.draw(screen, col * 75 + 37, row * 75 + 37)
    def handle_click(self, pos):
        col = pos[0] // 75
        row = pos[1] // 75
        if self.selected_candy:
            if (abs(self.selected_candy[0] - row) == 1 and self.selected_candy[1] == col) or \
               (abs(self.selected_candy[1] - col) == 1 and self.selected_candy[0] == row):
                self.swap_candies(self.selected_candy, (row, col))
                if not self.check_matches():
                    # Revert swap if no matches are found
                    self.swap_candies(self.selected_candy, (row, col))
                self.selected_candy = None
            else:
                self.selected_candy = (row, col)
        else:
            self.selected_candy = (row, col)