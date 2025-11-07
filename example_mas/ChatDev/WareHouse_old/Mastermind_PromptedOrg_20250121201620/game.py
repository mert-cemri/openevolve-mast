'''
This module contains the Game class, which manages the game logic, including setting up the game, processing guesses, and providing feedback.
'''
from color_sequence import ColorSequence
from feedback import Feedback
class Game:
    def __init__(self, sequence_length=4, max_tries=10):
        self.sequence_length = sequence_length
        self.max_tries = max_tries
        self.secret_sequence = ColorSequence.generate_random_sequence(sequence_length)
        self.tries = 0
    def start(self):
        print("Welcome to Mastermind!")
        print(f"Try to guess the {self.sequence_length}-color sequence.")
        print(f"You have {self.max_tries} attempts.")
        while self.tries < self.max_tries:
            guess = input(f"Attempt {self.tries + 1}: Enter your guess: ").strip().split()
            if len(guess) != self.sequence_length:
                print(f"Please enter exactly {self.sequence_length} colors.")
                continue
            if not all(color in ColorSequence.COLORS for color in guess):
                print(f"Please enter valid colors: {', '.join(ColorSequence.COLORS)}.")
                continue
            feedback = Feedback.evaluate(self.secret_sequence, guess)
            print(f"Feedback: {feedback['correct_position']} correct position, {feedback['correct_color']} correct color.")
            if feedback['correct_position'] == self.sequence_length:
                print("Congratulations! You've guessed the sequence!")
                return
            self.tries += 1
        print("Sorry, you've run out of attempts. Better luck next time!")
        print(f"The correct sequence was: {' '.join(self.secret_sequence)}")