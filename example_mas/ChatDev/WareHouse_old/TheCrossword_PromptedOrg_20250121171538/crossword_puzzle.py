'''
This file contains the CrosswordPuzzle and Clue classes, which manage the crossword grid, clues, and user interactions.
'''
class Clue:
    def __init__(self, number, direction, text, answer, start_row, start_col):
        self.number = number
        self.direction = direction
        self.text = text
        self.answer = answer
        self.start_row = start_row
        self.start_col = start_col
class CrosswordPuzzle:
    def __init__(self, grid_size, clues):
        self.grid_size = grid_size
        self.clues = {clue.number: clue for clue in clues}
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.correct_entries = {clue.number: False for clue in clues}
    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()
    def enter_word(self, clue_number, direction, word):
        if clue_number not in self.clues:
            print("Invalid clue number.")
            return False
        clue = self.clues[clue_number]
        if clue.direction != direction:
            print("Incorrect direction. Expected:", clue.direction)
            return False
        if len(word) != len(clue.answer):
            print("Incorrect word length. Expected length:", len(clue.answer))
            return False
        if self.validate_word(clue_number, direction, word):
            self.correct_entries[clue_number] = True
            self._fill_grid(clue_number, direction, word)
            return True
        print("Incorrect word. Try again.")
        return False
    def validate_word(self, clue_number, direction, word):
        clue = self.clues[clue_number]
        return word == clue.answer
    def _fill_grid(self, clue_number, direction, word):
        clue = self.clues[clue_number]
        if direction == 'across':
            row = clue.start_row
            col = clue.start_col
            for i, letter in enumerate(word):
                self.grid[row][col + i] = letter
        elif direction == 'down':
            row = clue.start_row
            col = clue.start_col
            for i, letter in enumerate(word):
                self.grid[row + i][col] = letter
    def check_completion(self):
        return all(self.correct_entries.values())