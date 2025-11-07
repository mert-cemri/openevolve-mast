'''
Contains the PuzzleGame class, managing game logic, puzzle state, and user interactions.
'''
from puzzle_data import PuzzleData
import random
class PuzzleGame:
    def __init__(self):
        self.words = []
        self.categories = {}
        self.found_groups = {}
        self.mistakes = 0
        self.max_mistakes = 4
    def generate_daily_puzzle(self):
        puzzle_data = PuzzleData.get_daily_puzzle()
        self.words = puzzle_data['words']
        self.categories = puzzle_data['categories']
        self.found_groups = {}
        self.mistakes = 0
        self.shuffle_words()
    def shuffle_words(self):
        random.shuffle(self.words)
    def select_group(self, selected_words):
        # Check if all selected words are still available in the puzzle grid
        if not all(word in self.words for word in selected_words):
            return False, "One or more selected words have already been grouped.", None
        selected_set = set(selected_words)
        for category, data in self.categories.items():
            if selected_set == set(data['words']):
                self.found_groups[category] = data
                for word in selected_words:
                    self.words.remove(word)
                return True, category, data['difficulty']
        self.mistakes += 1
        return False, None, None
    def is_game_over(self):
        return self.mistakes >= self.max_mistakes or len(self.words) == 0
    def display_grid(self):
        print("\nCurrent Puzzle Grid:")
        for i, word in enumerate(self.words):
            print(f"{word:<15}", end='\n' if (i+1) % 4 == 0 else '')
        print()