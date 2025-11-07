'''
Contains the StrandsGame class and related game logic functions.
'''
class StrandsGame:
    def __init__(self):
        # Initialize with some example strands
        self.strands = ["hel", "lo", "wor", "ld", "py", "thon"]
        self.valid_words = ["hello", "world", "python"]
        self.completed = []
    def check_combination(self, combination):
        # Check if the combination forms a valid word
        if combination in self.valid_words and combination not in self.completed:
            self.completed.append(combination)
            return True
        return False
    def is_complete(self):
        # Check if all valid words have been formed
        return set(self.completed) == set(self.valid_words)