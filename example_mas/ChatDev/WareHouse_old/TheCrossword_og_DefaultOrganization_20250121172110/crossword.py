'''
crossword.py
Contains the CrosswordGrid and Clue classes for managing the crossword puzzle logic.
'''
class Clue:
    def __init__(self, number, text, answer, start_row, start_col, direction):
        self.number = number
        self.text = text
        self.answer = answer
        self.start_row = start_row
        self.start_col = start_col
        self.direction = direction  # 'across' or 'down'
class CrosswordGrid:
    def __init__(self, size):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.clues = []
    def add_clue(self, clue):
        self.clues.append(clue)
    def validate_word(self, number, direction, word):
        for clue in self.clues:
            if clue.number == number and clue.direction == direction:
                correct_answer = clue.answer
                return word.lower() == correct_answer.lower()
        return False
    def fill_word(self, number, direction, word):
        for clue in self.clues:
            if clue.number == number and clue.direction == direction:
                if self.validate_word(number, direction, word):
                    row, col = clue.start_row, clue.start_col
                    for i, letter in enumerate(word):
                        if direction == 'across':
                            self.grid[row][col + i] = letter
                        elif direction == 'down':
                            self.grid[row + i][col] = letter
                    return True
                else:
                    # Provide feedback for incorrect word
                    print(f"Incorrect word for clue {number} {direction}. Please try again.")
                    return False
        return False
    def is_complete(self):
        for clue in self.clues:
            row, col = clue.start_row, clue.start_col
            for i, letter in enumerate(clue.answer):
                if clue.direction == 'across':
                    if self.grid[row][col + i] != letter:
                        return False
                elif clue.direction == 'down':
                    if self.grid[row + i][col] != letter:
                        return False
        return True