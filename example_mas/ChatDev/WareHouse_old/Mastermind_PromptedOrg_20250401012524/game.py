'''
Contains the MastermindGame class which handles game logic.
'''
import random
class MastermindGame:
    def __init__(self, code_length=4, max_attempts=10, digit_range=6):
        '''
        Initializes the Mastermind game with a random hidden code.
        '''
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.digit_range = digit_range
        self.hidden_code = self.generate_code()
    def generate_code(self):
        '''
        Generates a random hidden code consisting of digits from 0 to digit_range - 1.
        '''
        return ''.join(str(random.randint(0, self.digit_range - 1)) for _ in range(self.code_length))
    def evaluate_guess(self, guess):
        '''
        Evaluates the player's guess and returns a tuple of (exact_matches, partial_matches).
        '''
        exact_matches = sum(a == b for a, b in zip(self.hidden_code, guess))
        # Count occurrences of each digit in hidden code and guess for partial matches
        code_counts = [0] * self.digit_range
        guess_counts = [0] * self.digit_range
        for i in range(self.code_length):
            if self.hidden_code[i] != guess[i]:
                code_counts[int(self.hidden_code[i])] += 1
                guess_counts[int(guess[i])] += 1
        partial_matches = sum(min(code_counts[i], guess_counts[i]) for i in range(self.digit_range))
        return exact_matches, partial_matches
    def is_correct_guess(self, guess):
        '''
        Checks if the guess matches the hidden code exactly.
        '''
        return guess == self.hidden_code