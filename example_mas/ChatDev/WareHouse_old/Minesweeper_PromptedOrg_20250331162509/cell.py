'''
This file contains the Cell class, which represents individual cells on the board, storing information about whether they are mined, uncovered, or flagged.
'''
class Cell:
    def __init__(self):
        self.mine = False
        self.uncovered = False
        self.flagged = False
        self.adjacent_mines = 0
    def __str__(self):
        if self.flagged:
            return "F"
        if not self.uncovered:
            return "."
        if self.mine:
            return "*"
        return str(self.adjacent_mines)