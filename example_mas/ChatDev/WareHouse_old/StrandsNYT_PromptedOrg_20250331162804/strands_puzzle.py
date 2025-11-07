'''
Defines the StrandsPuzzle class and related functions for managing the puzzle.
'''
from grid import Grid
class StrandsPuzzle:
    def __init__(self, theme_words, spangram):
        self.grid = Grid()
        self.theme_words = theme_words
        self.spangram = spangram
        self.non_theme_words = []
        self.hints = 0
    def place_words(self):
        # Place the spangram on the grid
        self.grid.place_spangram(self.spangram)
        # Place theme words on the grid
        for word in self.theme_words:
            self.grid.place_word(word, highlight='blue')
    def highlight_word(self, word):
        self.grid.highlight(word)
    def check_word(self, word):
        # Check if the word can be formed on the grid
        if self.grid.can_form_word(word):
            if word not in self.theme_words and word != self.spangram:
                self.non_theme_words.append(word)
            return True
        return False
    def unlock_hint(self):
        # Unlock a hint for every 3 non-theme words found
        if len(self.non_theme_words) >= 3:
            self.hints += 1
            self.non_theme_words = []
            return True
        return False
    def is_completed(self):
        # Check if all theme words and the spangram are found
        return all(self.grid.is_word_highlighted(word) for word in self.theme_words + [self.spangram])
def load_words():
    # Load theme words and spangram from a data source
    theme_words = ["PYTHON", "JAVA", "JAVASCRIPT", "CPLUSPLUS"]
    spangram = "PROGRAMMING"
    return theme_words, spangram