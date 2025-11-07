'''
This module contains the Clue class, which represents a single clue in the crossword puzzle.
'''
class Clue:
    def __init__(self, number, direction, answer, start_row, start_col):
        self.number = number
        self.direction = direction
        self.answer = answer
        self.start_row = start_row
        self.start_col = start_col