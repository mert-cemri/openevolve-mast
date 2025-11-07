'''
This module contains the Grid class, which manages the grid of the crossword puzzle.
'''
class Grid:
    def __init__(self, rows, cols):
        # Initialize a grid with specified dimensions
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    def place_word(self, clue, word):
        # Place a word in the grid based on the clue
        if clue.direction == 'across':
            return self._place_across(clue, word)
        elif clue.direction == 'down':
            return self._place_down(clue, word)
        return False
    def _place_across(self, clue, word):
        # Place a word across the grid
        row, col = clue.start_row, clue.start_col
        if len(word) != len(clue.answer):
            return False
        for i, letter in enumerate(word):
            if self.grid[row][col + i] != ' ' and self.grid[row][col + i] != letter:
                return False
            self.grid[row][col + i] = letter
        return True
    def _place_down(self, clue, word):
        # Place a word down the grid
        row, col = clue.start_row, clue.start_col
        if len(word) != len(clue.answer):
            return False
        for i, letter in enumerate(word):
            if self.grid[row + i][col] != ' ' and self.grid[row + i][col] != letter:
                return False
            self.grid[row + i][col] = letter
        return True
    def check_word(self, clue):
        # Check if a word matches the clue in the grid
        if clue.direction == 'across':
            return self._check_across(clue)
        elif clue.direction == 'down':
            return self._check_down(clue)
        return False
    def _check_across(self, clue):
        # Check a word across the grid
        row, col = clue.start_row, clue.start_col
        word = ''.join(self.grid[row][col + i] for i in range(len(clue.answer)))
        return word == clue.answer
    def _check_down(self, clue):
        # Check a word down the grid
        row, col = clue.start_row, clue.start_col
        word = ''.join(self.grid[row + i][col] for i in range(len(clue.answer)))
        return word == clue.answer