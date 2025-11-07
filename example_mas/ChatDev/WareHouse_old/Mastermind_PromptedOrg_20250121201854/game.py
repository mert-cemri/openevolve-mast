'''
This module contains the Game class, which manages the Mastermind game logic, including code generation, handling guesses, and providing feedback.
'''
import random
class Game:
    def __init__(self, code_length=4, max_attempts=10):
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.hidden_code = self.generate_code()
        self.attempts = 0
    def generate_code(self):
        # Generates a random sequence of digits as the hidden code
        return [random.choice('0123456789') for _ in range(self.code_length)]
    def make_guess(self, guess):
        self.attempts += 1
        feedback = self.provide_feedback(guess)
        return feedback
    def provide_feedback(self, guess):
        # Provides feedback on the guess in terms of correct color and correct position
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.hidden_code[i])
        correct_color = sum(min(guess.count(x), self.hidden_code.count(x)) for x in set(guess)) - correct_position
        return correct_position, correct_color
    def is_game_over(self, last_guess=None):
        if last_guess and last_guess == self.hidden_code:
            return True
        return self.attempts >= self.max_attempts