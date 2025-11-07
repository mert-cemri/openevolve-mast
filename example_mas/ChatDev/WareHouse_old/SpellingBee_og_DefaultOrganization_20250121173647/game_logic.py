'''
Game logic for the Spelling Bee puzzle game.
'''
class SpellingBeeGame:
    def __init__(self, central_letter, other_letters):
        self.central_letter = central_letter
        self.other_letters = other_letters
        self.all_letters = set(other_letters + [central_letter])
    def is_valid_word(self, word):
        if len(word) < 4:
            return False
        if self.central_letter not in word:
            return False
        if not set(word).issubset(self.all_letters):
            return False
        return True
    def calculate_score(self, word):
        if len(set(word)) == 7:
            return len(word) + 7  # Bonus for using all letters
        return len(word)