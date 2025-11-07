'''
This file contains the Puzzle class, which stores the words and their correct categories, and provides methods to check if a user's guess is correct.
'''
from category import Category
class Puzzle:
    def __init__(self):
        self.categories = [
            Category("Fruits", ["apple", "banana", "orange", "grape"]),
            Category("Colors", ["red", "blue", "green", "yellow"]),
            Category("Animals", ["cat", "dog", "lion", "tiger"]),
            Category("Countries", ["usa", "canada", "mexico", "brazil"])
        ]
        self.solved_categories = []
    def check_guess(self, guess):
        for category in self.categories:
            if category.is_correct_group(guess) and category not in self.solved_categories:
                self.solved_categories.append(category)
                return True
        return False
    def is_solved(self):
        return len(self.solved_categories) == 4