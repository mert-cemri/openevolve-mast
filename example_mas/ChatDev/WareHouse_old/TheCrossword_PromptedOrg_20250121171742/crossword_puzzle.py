'''
This module contains the CrosswordPuzzle class, which represents the crossword puzzle and manages the grid and clues.
'''
from grid import Grid
from clue import Clue
class CrosswordPuzzle:
    def __init__(self):
        self.clues = self._initialize_clues()
        max_row, max_col = self._calculate_grid_size()
        self.grid = Grid(max_row, max_col)
    def _initialize_clues(self):
        # Initialize clues with numbers, directions, answers, and starting coordinates
        return [
            Clue(1, 'across', 'hello', 0, 0),
            Clue(2, 'down', 'world', 0, 1),
            # Add more clues as needed with appropriate starting coordinates
        ]
    def _calculate_grid_size(self):
        # Calculate the necessary grid size based on the clues
        max_row = max(clue.start_row + (len(clue.answer) if clue.direction == 'down' else 1) for clue in self.clues)
        max_col = max(clue.start_col + (len(clue.answer) if clue.direction == 'across' else 1) for clue in self.clues)
        return max_row, max_col
    def is_completed(self):
        # Check if all words are correctly filled in the grid
        for clue in self.clues:
            if not self.grid.check_word(clue):
                return False
        return True
    def enter_word(self, clue_number, direction, word):
        # Enter a word into the grid based on the clue number and direction
        for clue in self.clues:
            if clue.number == clue_number and clue.direction == direction:
                return self.grid.place_word(clue, word)
        return False