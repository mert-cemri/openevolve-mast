'''
This module contains the Game class, which manages the game logic for the word categorization puzzle.
'''
class Game:
    def __init__(self):
        # Define the categories and words
        self.categories = {
            "Fruits": ["Apple", "Banana", "Orange", "Grape"],
            "Animals": ["Dog", "Cat", "Elephant", "Tiger"],
            "Colors": ["Red", "Blue", "Green", "Yellow"],
            "Countries": ["USA", "Canada", "India", "China"]
        }
        self.words = [word for category in self.categories.values() for word in category]
        self.correct_groups = []
        self.max_tries = 10
        self.tries = 0
    def check_group(self, selected_words):
        # Check if the selected words form a valid group
        for category, words in self.categories.items():
            if set(selected_words) == set(words):
                if category not in self.correct_groups:
                    self.correct_groups.append(category)
                    return True, category
        return False, None
    def is_game_over(self):
        # Check if the game is over
        return len(self.correct_groups) == len(self.categories) or self.tries >= self.max_tries
    def increment_tries(self):
        # Increment the number of tries
        self.tries += 1