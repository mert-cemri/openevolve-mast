'''
This file contains the Board class which handles the representation of the game board.
'''
class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    def display(self):
        for i, row in enumerate(self.grid):
            print('|'.join(row))
            if i < 2:  # Only print the line after the first two rows
                print('-' * 5)
    def update(self, row, col, player):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = player
            return True
        return False