'''
Defines the StrandPuzzle class which contains the logic for the Strands puzzle game.
'''
import itertools
class StrandPuzzle:
    def __init__(self, strands, valid_words):
        '''
        Initializes the puzzle with given strands and valid words.
        :param strands: List of strands to be combined.
        :param valid_words: Set of valid words or phrases.
        '''
        self.strands = strands
        self.valid_words = set(valid_words)
        self.valid_combinations = self.generate_valid_combinations()
        self.used_combinations = set()
    def generate_valid_combinations(self):
        '''
        Generates all possible valid combinations from the strands.
        :return: List of valid combinations.
        '''
        possible_combinations = set()
        for i in range(1, len(self.strands) + 1):
            for combination in itertools.permutations(self.strands, i):
                combined_str = ''.join(combination)
                if combined_str in self.valid_words:
                    possible_combinations.add(combined_str)
        return possible_combinations
    def is_valid_combination(self, combination):
        '''
        Checks if a given combination of strands forms a valid word or phrase.
        :param combination: The combination of strands to check.
        :return: True if valid, False otherwise.
        '''
        if combination in self.valid_combinations:
            self.used_combinations.add(combination)
            return True
        return False
    def is_completed(self):
        '''
        Checks if all strands have been correctly merged.
        :return: True if completed, False otherwise.
        '''
        return self.valid_combinations == self.used_combinations