'''
This file contains the Cell class, which represents each cell on the Minesweeper board.
'''
class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_uncovered = False
        self.adjacent_mines = 0