'''
Core logic for the Wordle game, including daily word selection, guess validation, and feedback generation.
'''
import random
from datetime import datetime
class WordleGame:
    def __init__(self, word_list):
        self.word_list = word_list
        # Use current date as seed to ensure daily consistency
        today = datetime.now().strftime("%Y-%m-%d")
        random.seed(today)
        self.target_word = random.choice(self.word_list)
    def validate_guess(self, guess):
        return len(guess) == 5 and guess in self.word_list
    def get_feedback(self, guess):
        feedback = []
        target_word_temp = list(self.target_word)
        # First pass for correct letters in correct positions (green)
        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                feedback.append(f"\033[92m{letter.upper()}\033[0m")  # Green
                target_word_temp[i] = None  # Mark as used
            else:
                feedback.append(None)  # Placeholder for second pass
        # Second pass for correct letters in wrong positions (yellow) and incorrect letters (grey)
        for i, letter in enumerate(guess):
            if feedback[i] is None:
                if letter in target_word_temp:
                    feedback[i] = f"\033[93m{letter.upper()}\033[0m"  # Yellow
                    target_word_temp[target_word_temp.index(letter)] = None  # Mark as used
                else:
                    feedback[i] = f"\033[90m{letter.upper()}\033[0m"  # Grey
        return ' '.join(feedback)
    def is_correct_guess(self, guess):
        return guess == self.target_word