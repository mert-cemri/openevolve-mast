'''
This module defines the CrosswordPuzzle and Clue classes for managing the crossword puzzle grid and clues.
'''
class Clue:
    def __init__(self, number, direction, position, answer):
        '''
        Initialize a clue with its number, direction, starting position, and answer.
        '''
        self.number = number
        self.direction = direction
        self.position = position
        self.answer = answer
class CrosswordPuzzle:
    def __init__(self, grid_size, clues):
        '''
        Initialize the crossword puzzle with a grid size and a list of clues.
        '''
        self.grid_size = grid_size
        self.clues = {clue.number: clue for clue in clues}
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    def add_word(self, clue_number, direction, word):
        '''
        Add a word to the grid based on the clue number and direction.
        '''
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
        '''
        Validate if the word matches the clue and does not conflict with existing letters on the grid.
        '''
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
    def is_complete(self):
        '''
        Check if the crossword puzzle is complete.
        '''
        for clue in self.clues.values():
            x, y = clue.position
            for i, char in enumerate(clue.answer):
                if clue.direction == 'across' and self.grid[x][y + i] != char:
                    return False
                elif clue.direction == 'down' and self.grid[x + i][y] != char:
                    return False
        return True
    def display_grid(self):
        '''
        Display the current state of the crossword grid.
        '''
        print("Current Crossword Grid:")
        for row in self.grid:
            print(' '.join(row))
        print()
    def display_clues(self):
        '''
        Display all clues with their numbers, directions, and positions.
        '''
        print("Clues:")
        for clue in self.clues.values():
            print(f"Clue {clue.number}: {clue.direction} starting at {clue.position}")
        print()