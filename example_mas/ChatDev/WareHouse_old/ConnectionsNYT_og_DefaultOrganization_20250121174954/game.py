'''
Contains the Game class which manages the game logic and state.
'''
from word_category import WordCategory
class Game:
    def __init__(self):
        # Define categories and words
        self.categories = [
            WordCategory("Fruits", ["apple", "banana", "orange", "grape"]),
            WordCategory("Animals", ["lion", "tiger", "bear", "wolf"]),
            WordCategory("Colors", ["red", "blue", "green", "yellow"]),
            WordCategory("Countries", ["usa", "canada", "mexico", "brazil"])
        ]
        self.words = [word for category in self.categories for word in category.words]
        self.attempts = 0
        self.max_attempts = 10
        self.correct_groups = 0
        self.completed_categories = []  # Track completed categories
    def check_guess(self, guess):
        # Check if the guess is a valid group and hasn't been guessed before
        for category in self.categories:
            if set(guess) == set(category.words) and category not in self.completed_categories:
                self.correct_groups += 1
                self.completed_categories.append(category)
                return True, []
        # Provide feedback on which words are correct
        correct_words = []
        for word in guess:
            for category in self.categories:
                if word in category.words:
                    correct_words.append(word)
                    break
        return False, correct_words
    def is_game_over(self):
        return self.correct_groups == len(self.categories) or self.attempts >= self.max_attempts