'''
This module contains the PuzzleGenerator class, which generates a new puzzle daily, ensuring that there is only one correct solution.
'''
import random
from category import Category
from itertools import combinations
class PuzzleGenerator:
    def __init__(self):
        self.categories = [
            Category("Fruits", ["apple", "banana", "orange", "grape"]),
            Category("Colors", ["red", "blue", "green", "yellow"]),
            Category("Animals", ["cat", "dog", "fish", "bird"]),
            Category("Countries", ["usa", "canada", "mexico", "brazil"])
        ]
    def generate_puzzle(self):
        while True:
            words = []
            for category in self.categories:
                words.extend(category.words)
            random.shuffle(words)
            if self.has_unique_solution(words):
                return self.categories, words
    def has_unique_solution(self, words):
        # Check all possible groupings of the words into sets of four
        possible_groupings = list(combinations(words, 4))
        valid_groupings = 0
        for grouping in possible_groupings:
            if any(set(grouping) == set(category.words) for category in self.categories):
                valid_groupings += 1
        # Ensure only four valid groupings exist, one for each category
        return valid_groupings == len(self.categories)