'''
This module contains the CrosswordPuzzle and Clue classes for managing the crossword puzzle logic.
'''
class Clue:
    def __init__(self, number, direction, answer, position):
        self.number = number
        self.direction = direction
        self.answer = answer
        self.position = position
class CrosswordPuzzle:
    def __init__(self, grid_size, clues):
        self.grid_size = grid_size
        self.clues = {clue.number: clue for clue in clues}
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()
    def enter_word(self, clue_number, direction, word):
        if clue_number not in self.clues:
            return False
        clue = self.clues[clue_number]
        if clue.direction != direction or len(word) != len(clue.answer):
            return False
        if not self.validate_word(clue_number, direction, word):
            return False
        x, y = clue.position
        for i, char in enumerate(word):
            if direction == 'across':
                self.grid[x][y + i] = char
            elif direction == 'down':
                self.grid[x + i][y] = char
        return True
    def validate_word(self, clue_number, direction, word):
        clue = self.clues[clue_number]
        x, y = clue.position
        for i, char in enumerate(word):
            if direction == 'across':
                if self.grid[x][y + i] != ' ' and self.grid[x][y + i] != char:
                    return False
            elif direction == 'down':
                if self.grid[x + i][y] != ' ' and self.grid[x + i][y] != char:
                    return False
        return word == clue.answer
    def check_completion(self):
        for clue in self.clues.values():
            x, y = clue.position
            for i, char in enumerate(clue.answer):
                if clue.direction == 'across' and self.grid[x][y + i] != char:
                    return False
                elif clue.direction == 'down' and self.grid[x + i][y] != char:
                    return False
        return True