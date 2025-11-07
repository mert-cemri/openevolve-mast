'''
CrosswordPuzzle class manages crossword puzzle grid, clues, and answers.
'''
class CrosswordPuzzle:
    def __init__(self):
        # Define a simple crossword puzzle grid (5x5) for demonstration
        self.grid = [
            ['C', 'A', 'T', '', ''],
            ['', '', 'A', '', ''],
            ['D', 'O', 'G', '', ''],
            ['', '', 'E', '', ''],
            ['', '', 'R', 'A', 'T']
        ]
        # User's current grid state (initially empty)
        self.user_grid = [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_']
        ]
        # Clues for across and down
        self.clues_across = {
            1: "A small domesticated feline animal (3 letters)",
            3: "A small domesticated canine animal (3 letters)",
            5: "A small rodent animal (3 letters)"
        }
        self.clues_down = {
            2: "Opposite of off (2 letters)",
            4: "To consume food (3 letters)"
        }
        # Answers for validation
        self.answers_across = {
            1: ("CAT", (0, 0)),
            3: ("DOG", (2, 0)),
            5: ("RAT", (4, 2))
        }
        self.answers_down = {
            2: ("AT", (0, 1)),
            4: ("EAT", (1, 2))
        }
    def display_grid(self):
        print("\nCurrent Crossword Grid:")
        for row in self.user_grid:
            print(' '.join(row))
        print()
    def display_clues(self):
        print("\nAcross Clues:")
        for num, clue in self.clues_across.items():
            print(f"{num}. {clue}")
        print("\nDown Clues:")
        for num, clue in self.clues_down.items():
            print(f"{num}. {clue}")
        print()
    def enter_word(self, clue_number, direction, word):
        word = word.upper()
        if self.validate_word(clue_number, direction, word):
            if direction == 'across':
                _, (row, col) = self.answers_across[clue_number]
                for i, letter in enumerate(word):
                    self.user_grid[row][col + i] = letter
            elif direction == 'down':
                _, (row, col) = self.answers_down[clue_number]
                for i, letter in enumerate(word):
                    self.user_grid[row + i][col] = letter
            print("Correct! Word added to the grid.")
        else:
            print("Incorrect word or word placement. Please try again.")
    def validate_word(self, clue_number, direction, word):
        word = word.upper()
        if direction == 'across':
            answer, (row, col) = self.answers_across.get(clue_number, ("", ()))
            if not answer:
                print("Invalid clue number for across direction.")
                return False
            if len(word) != len(answer):
                print(f"Incorrect word length. Expected {len(answer)} letters.")
                return False
            if col + len(word) > len(self.grid[0]):
                print("Word exceeds grid boundaries horizontally.")
                return False
            for i, letter in enumerate(word):
                correct_letter = answer[i]
                existing_letter = self.user_grid[row][col + i]
                if existing_letter != '_' and existing_letter != letter:
                    print(f"Letter conflict at position ({row}, {col + i}). Expected '{existing_letter}', got '{letter}'.")
                    return False
                if letter != correct_letter:
                    print(f"Incorrect letter '{letter}' at position ({row}, {col + i}). Expected '{correct_letter}'.")
                    return False
        elif direction == 'down':
            answer, (row, col) = self.answers_down.get(clue_number, ("", ()))
            if not answer:
                print("Invalid clue number for down direction.")
                return False
            if len(word) != len(answer):
                print(f"Incorrect word length. Expected {len(answer)} letters.")
                return False
            if row + len(word) > len(self.grid):
                print("Word exceeds grid boundaries vertically.")
                return False
            for i, letter in enumerate(word):
                correct_letter = answer[i]
                existing_letter = self.user_grid[row + i][col]
                if existing_letter != '_' and existing_letter != letter:
                    print(f"Letter conflict at position ({row + i}, {col}). Expected '{existing_letter}', got '{letter}'.")
                    return False
                if letter != correct_letter:
                    print(f"Incorrect letter '{letter}' at position ({row + i}, {col}). Expected '{correct_letter}'.")
                    return False
        else:
            print("Invalid direction specified.")
            return False
        return True
    def check_completion(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] != '':
                    if self.user_grid[i][j] != self.grid[i][j]:
                        return False
        return True