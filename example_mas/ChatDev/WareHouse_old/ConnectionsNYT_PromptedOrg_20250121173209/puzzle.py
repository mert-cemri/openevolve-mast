'''
This module defines the Puzzle class, which represents the puzzle and manages the game logic.
'''
from category import Category
import random
class Puzzle:
    def __init__(self):
        # Define categories and words
        self.categories = [
            Category("Fruits", ["apple", "banana", "orange", "grape"]),
            Category("Colors", ["red", "blue", "green", "yellow"]),
            Category("Animals", ["cat", "dog", "lion", "tiger"]),
            Category("Countries", ["usa", "canada", "mexico", "brazil"])
        ]
        self.all_words = [word for category in self.categories for word in category.words]
        self.shuffled_words = random.sample(self.all_words, len(self.all_words))
        self.remaining_tries = 10
        self.solved_categories = []
    def get_shuffled_words(self):
        return self.shuffled_words
    def check_guess(self, guess):
        # Normalize the case and strip spaces for the guessed words
        guess_lower = [word.strip().lower() for word in guess]
        for category in self.categories:
            # Normalize the case for the category words
            category_words_lower = [word.lower() for word in category.words]
            if set(guess_lower) == set(category_words_lower) and category not in self.solved_categories:
                self.solved_categories.append(category)
                self.shuffled_words = [word for word in self.shuffled_words if word.lower() not in guess_lower]
                return True
        incorrect_words = [word for word in guess if word.lower() not in self.all_words]
        if incorrect_words:
            print(f"These words are incorrect or not part of any category: {', '.join(incorrect_words)}")
        self.remaining_tries -= 1
        return False
    def is_solved(self):
        return len(self.solved_categories) == len(self.categories)