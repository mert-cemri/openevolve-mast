'''
Crossword grid and clue management.
'''
class CrosswordGrid:
    def __init__(self, rows, cols, clues):
        self.rows = rows
        self.cols = cols
        self.grid = [['' for _ in range(cols)] for _ in range(rows)]
        self.clues = clues
    def add_word(self, clue, word):
        if clue.direction == 'across':
            for j, letter in enumerate(word):
                self.grid[clue.start_row][clue.start_col + j] = letter
        elif clue.direction == 'down':
            for i, letter in enumerate(word):
                self.grid[clue.start_row + i][clue.start_col] = letter
    def validate_word(self, clue, word):
        if len(word) != len(clue.answer):
            return False
        for i, letter in enumerate(word):
            if clue.direction == 'across':
                if self.grid[clue.start_row][clue.start_col + i] not in ('', letter):
                    return False
            elif clue.direction == 'down':
                if self.grid[clue.start_row + i][clue.start_col] not in ('', letter):
                    return False
        if clue.answer == word:
            self.add_word(clue, word)
            return True
        return False
    def is_complete(self):
        for clue in self.clues:
            word = ""
            if clue.direction == 'across':
                for j in range(len(clue.answer)):
                    word += self.grid[clue.start_row][clue.start_col + j]
            elif clue.direction == 'down':
                for i in range(len(clue.answer)):
                    word += self.grid[clue.start_row + i][clue.start_col]
            if word != clue.answer:
                return False
        return True
class Clue:
    def __init__(self, number, direction, text, answer, start_row, start_col):
        self.number = number
        self.direction = direction
        self.text = text
        self.answer = answer
        self.start_row = start_row
        self.start_col = start_col