'''
This file contains the Game class which manages the game logic and state.
'''
from category import Category
class Game:
    def __init__(self, words, categories):
        self.words = words
        self.categories = {name: Category(words) for name, words in categories.items()}
        self.attempts = 0
        self.max_attempts = 10
        self.found_categories = []
    def check_guess(self, guess):
        for name, category in self.categories.items():
            if category.contains(guess) and name not in self.found_categories:
                self.found_categories.append(name)
                return True
        return False
    def is_game_over(self):
        return len(self.found_categories) == len(self.categories) or self.attempts >= self.max_attempts
    def play(self, ui):
        while not self.is_game_over():
            guess = ui.get_user_input()
            if self.check_guess(guess):
                ui.display_message("Correct group!")
            else:
                ui.display_message("Incorrect group.")
            self.attempts += 1
        if len(self.found_categories) == len(self.categories):
            ui.display_message("Congratulations! You've found all groups.")
        else:
            ui.display_message("Game over. Better luck next time!")