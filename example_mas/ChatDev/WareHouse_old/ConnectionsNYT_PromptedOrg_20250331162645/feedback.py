'''
This module contains the Feedback class, which provides immediate feedback to the player after each guess.
'''
class Feedback:
    def correct_guess(self):
        print("Correct! You've found a valid group.")
    def incorrect_guess(self):
        print("Incorrect guess. Try again.")