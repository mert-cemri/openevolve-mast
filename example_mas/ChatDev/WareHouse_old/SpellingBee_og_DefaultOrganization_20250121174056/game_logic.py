'''
Game logic for the Spelling Bee puzzle game.
'''
import random
class SpellingBeeGame:
    def __init__(self):
        self.central_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
        self.surrounding_letters = random.sample(
            [letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter != self.central_letter], 6
        )
        # Ensure the central letter is included in the surrounding letters
        if self.central_letter not in self.surrounding_letters:
            self.surrounding_letters.append(self.central_letter)
            random.shuffle(self.surrounding_letters)
    def is_valid_word(self, word):
        if len(word) < 4 or self.central_letter not in word:
            return False
        for letter in word:
            if letter not in self.surrounding_letters:
                return False
        return True
    def calculate_score(self, word):
        return len(word) - 3