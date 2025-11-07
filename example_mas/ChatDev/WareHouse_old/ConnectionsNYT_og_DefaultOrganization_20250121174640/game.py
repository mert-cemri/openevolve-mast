'''
Contains the Game class which manages the game logic and state.
'''
class Game:
    def __init__(self):
        # Define words and their categories
        self.categories = {
            "Fruits": ["Apple", "Banana", "Orange", "Grape"],
            "Animals": ["Dog", "Cat", "Elephant", "Lion"],
            "Colors": ["Red", "Blue", "Green", "Yellow"],
            "Countries": ["USA", "Canada", "Mexico", "Brazil"]
        }
        self.words = [word for category in self.categories.values() for word in category]
        self.correct_groups = []
        self.max_tries = 10
        self.tries = 0
    def check_guess(self, guess):
        # Check if the guess is a valid group
        for category, words in self.categories.items():
            if set(guess) == set(words):
                if category not in self.correct_groups:
                    self.correct_groups.append(category)
                    return True, f"Correct! You've found the {category} category."
        self.tries += 1
        return False, "Incorrect group. Try again."
    def is_game_over(self):
        # Check if the game is over
        return len(self.correct_groups) == len(self.categories) or self.tries >= self.max_tries