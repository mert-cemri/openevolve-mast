'''
DOCSTRING: Manages the Spelling Bee game logic, including initialization, user input validation, and score tracking.
'''
from word_validator import WordValidator
from score_tracker import ScoreTracker
from user_interface import UserInterface
class SpellingBeeGame:
    def __init__(self, central_letter, surrounding_letters, valid_words):
        self.central_letter = central_letter
        self.surrounding_letters = surrounding_letters
        self.letters = [self.central_letter] + self.surrounding_letters
        self.validator = WordValidator(self.central_letter, self.letters, valid_words)
        self.score_tracker = ScoreTracker()
        self.ui = UserInterface()
    def start(self):
        self.ui.display_welcome_message(self.central_letter, self.surrounding_letters)
        while True:
            word = self.ui.get_user_input()
            if word == 'exit':
                break
            if self.validator.is_valid(word):
                score = self.score_tracker.calculate_score(word)
                self.ui.display_score(score)
            else:
                self.ui.display_invalid_word_message()