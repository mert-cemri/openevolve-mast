'''
This file contains the MinesweeperGame class, which manages the game logic and board state.
'''
import random
from cell import Cell
class MinesweeperGame:
    def __init__(self):
        self.size = 9
        self.mines_count = 10
        self.board = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.place_mines()
        self.calculate_adjacent_mines()
    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines_count:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if not self.board[row][col].is_mine:
                self.board[row][col].is_mine = True
                mines_placed += 1
    def calculate_adjacent_mines(self):
        for row in range(self.size):
            for col in range(self.size):
                if not self.board[row][col].is_mine:
                    self.board[row][col].adjacent_mines = self.count_adjacent_mines(row, col)
    def count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row-1), min(self.size, row+2)):
            for c in range(max(0, col-1), min(self.size, col+2)):
                if self.board[r][c].is_mine:
                    count += 1
        return count
    def uncover_cell(self, row, col):
        if self.board[row][col].is_uncovered:
            print("This cell is already uncovered. Try a different cell.")
            return False
        self.board[row][col].is_uncovered = True
        if self.board[row][col].is_mine:
            return True
        if self.board[row][col].adjacent_mines == 0:
            for r in range(max(0, row-1), min(self.size, row+2)):
                for c in range(max(0, col-1), min(self.size, col+2)):
                    if not self.board[r][c].is_uncovered:
                        self.uncover_cell(r, c)
        return False
    def check_win(self):
        for row in range(self.size):
            for col in range(self.size):
                if not self.board[row][col].is_mine and not self.board[row][col].is_uncovered:
                    return False
        return True
    def display_board(self):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for row in range(self.size):
            print(row, end=' ')
            for col in range(self.size):
                cell = self.board[row][col]
                if cell.is_uncovered:
                    if cell.is_mine:
                        print('*', end=' ')
                    else:
                        print(cell.adjacent_mines, end=' ')
                else:
                    print('.', end=' ')
            print()