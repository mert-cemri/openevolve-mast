'''
This file contains the Board class, which represents the game board, handles cell operations (uncovering, flagging), and manages mine placement.
'''
from cell import Cell
import random
class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.setup_board()
    def setup_board(self):
        if self.difficulty == "beginner":
            self.size = 9
            self.mines = 10
        elif self.difficulty == "intermediate":
            self.size = 16
            self.mines = 40
        elif self.difficulty == "expert":
            self.size = 24
            self.mines = 99
        else:
            raise ValueError("Invalid difficulty level")
        self.grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.place_mines()
    def place_mines(self):
        mine_positions = random.sample(range(self.size * self.size), self.mines)
        for pos in mine_positions:
            x, y = divmod(pos, self.size)
            self.grid[x][y].mine = True
    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
    def uncover(self, x, y):
        if self.grid[x][y].mine:
            return True
        self.flood_fill(x, y)
        return False
    def flood_fill(self, x, y):
        if not (0 <= x < self.size and 0 <= y < self.size):
            return
        cell = self.grid[x][y]
        if cell.uncovered or cell.flagged:
            return
        cell.uncovered = True
        adjacent_mines = self.count_adjacent_mines(x, y)
        if adjacent_mines == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        self.flood_fill(x + dx, y + dy)
        else:
            cell.adjacent_mines = adjacent_mines
    def count_adjacent_mines(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny].mine:
                    count += 1
        return count
    def flag(self, x, y):
        self.grid[x][y].flagged = not self.grid[x][y].flagged
    def is_cleared(self):
        for row in self.grid:
            for cell in row:
                if not cell.mine and not cell.uncovered:
                    return False
        return True