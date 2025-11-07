'''
This module defines the CrosswordPuzzle class, which manages the crossword puzzle grid, clues, and solutions.
'''
class CrosswordPuzzle:
    def __init__(self):
        # Grid representation (5x5 example)
        self.grid = [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_']
        ]
        # Revised solutions for across and down clues
        self.solutions = {
            'across': {
                1: ('HELLO', (0, 0)),
                3: ('WORLD', (2, 0))
            },
            'down': {
                2: ('OCEAN', (0, 2)),
                4: ('LOW', (0, 4))
            }
        }
        # Revised clues for across and down
        self.clues = {
            'across': {
                1: 'Greeting word',
                3: 'The earth, collectively'
            },
            'down': {
                2: 'Large body of salt water',
                4: 'Opposite of high'
            }
        }
    def display_grid(self):
        print("\nCurrent Crossword Grid:")
        for row in self.grid:
            print(' '.join(row))
        print()
    def display_clues(self):
        print("Across Clues:")
        for num, clue in self.clues['across'].items():
            print(f"{num}. {clue}")
        print("\nDown Clues:")
        for num, clue in self.clues['down'].items():
            print(f"{num}. {clue}")
        print()
    def enter_word(self, clue_number, direction, word):
        direction = direction.lower()
        if clue_number not in self.solutions[direction]:
            print("Invalid clue number or direction.")
            return False
        solution, (row, col) = self.solutions[direction][clue_number]
        word = word.upper()
        if len(word) != len(solution):
            print("Incorrect word length.")
            return False
        # Validate letters match existing letters in grid and check boundaries
        for i, letter in enumerate(word):
            r, c = (row, col + i) if direction == 'across' else (row + i, col)
            if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
                print(f"Word '{word}' exceeds grid boundaries at position ({r+1},{c+1}).")
                return False
            if self.grid[r][c] != '_' and self.grid[r][c] != letter:
                print(f"Letter mismatch at position ({r+1},{c+1}).")
                return False
        # Update grid with the entered word
        for i, letter in enumerate(word):
            r, c = (row, col + i) if direction == 'across' else (row + i, col)
            self.grid[r][c] = letter
        print("Word accepted!")
        return True
    def is_completed(self):
        for direction in self.solutions:
            for clue_number, (solution, (row, col)) in self.solutions[direction].items():
                for i, letter in enumerate(solution):
                    r, c = (row, col + i) if direction == 'across' else (row + i, col)
                    if self.grid[r][c] != letter:
                        return False
        return True