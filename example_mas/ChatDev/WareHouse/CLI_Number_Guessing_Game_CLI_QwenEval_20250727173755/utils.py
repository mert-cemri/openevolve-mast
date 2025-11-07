'''
Utility functions for the Number Guessing Game.
This module provides helper functions for generating random numbers
and obtaining user input, ensuring that the input is valid.
'''
import random
def get_user_guess(lower_bound, upper_bound):
    while True:
        try:
            guess = int(input(f"Enter your guess ({lower_bound}-{upper_bound}): "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def generate_random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)