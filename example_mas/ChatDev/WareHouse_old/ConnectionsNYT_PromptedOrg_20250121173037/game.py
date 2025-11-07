'''
This file contains the Game class, which manages the overall game logic, including initializing the game, handling user guesses, and checking for win conditions.
'''
from puzzle import Puzzle
from user_interface import UserInterface
class Game:
    def __init__(self):
        self.puzzle = Puzzle()
        self.ui = UserInterface()
        self.max_tries = 10
        self.tries = 0
    def start(self):
        self.ui.display_welcome_message()
        while not self.puzzle.is_solved() and self.tries < self.max_tries:
            guess = self.ui.get_user_guess()
            if self.puzzle.check_guess(guess):
                self.ui.display_correct_guess_message()
            else:
                self.ui.display_incorrect_guess_message()
            self.tries += 1
        self.ui.display_end_message(self.puzzle.is_solved())