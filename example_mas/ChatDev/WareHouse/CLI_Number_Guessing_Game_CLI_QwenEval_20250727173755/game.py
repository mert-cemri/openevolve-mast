'''
Contains the logic for the Number Guessing Game.
This module defines the game mechanics, including generating a random number,
handling user input, and providing feedback based on the user's guesses.
'''
import random
from utils import get_user_guess, generate_random_number
class NumberGuessingGame:
    def __init__(self, lower_bound=1, upper_bound=100, max_attempts=10):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = generate_random_number(lower_bound, upper_bound)
        self.attempts = 0
        self.max_attempts = max_attempts
    def play_game(self):
        print(f"\nI have selected a number between {self.lower_bound} and {self.upper_bound}.")
        print(f"You have {self.max_attempts} attempts to guess the number.")
        # Loop until the user either guesses the number or runs out of attempts
        while self.attempts < self.max_attempts:
            remaining_attempts = self.max_attempts - self.attempts
            print(f"Attempts left: {remaining_attempts}")
            guess = get_user_guess(self.lower_bound, self.upper_bound)
            self.attempts += 1
            # Check if the guess is lower, higher, or correct
            if guess < self.secret_number:
                print("Too low! Try again.")
            elif guess > self.secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {self.attempts} attempts.")
                return
        # If the user runs out of attempts, reveal the secret number
        print(f"Sorry, you've used all your attempts. The number was {self.secret_number}.")