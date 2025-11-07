'''
This module contains the SpellingBeeGame class which manages the game logic for the Spelling Bee puzzle.
'''
class SpellingBeeGame:
    def __init__(self, central_letter, surrounding_letters):
        self.central_letter = central_letter
        self.surrounding_letters = surrounding_letters
        self.valid_letters = set(surrounding_letters + [central_letter])
        self.found_words = []
        self.score = 0
    def is_valid_word(self, word):
        if len(word) < 4:
            return False, "Word is too short."
        if self.central_letter not in word:
            return False, "Word does not contain the central letter."
        if not set(word).issubset(self.valid_letters):
            return False, "Word uses invalid letters."
        return True, ""
    def calculate_score(self, word):
        base_score = len(word)
        bonus = 0
        if len(word) >= 7:
            bonus = 5
        return base_score + bonus
    def add_word(self, word):
        is_valid, message = self.is_valid_word(word)
        if is_valid and word not in self.found_words:
            self.found_words.append(word)
            self.score += self.calculate_score(word)
            return True, "Good job! Word accepted."
        return False, message
    def get_feedback(self):
        return f"Words found: {len(self.found_words)}, Score: {self.score}"