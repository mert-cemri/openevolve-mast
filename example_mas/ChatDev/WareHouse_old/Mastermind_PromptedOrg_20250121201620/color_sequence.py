'''
This module contains the ColorSequence class, which represents the sequence of colors (or digits) that the computer selects and the player guesses.
'''
import random
class ColorSequence:
    COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    @staticmethod
    def generate_random_sequence(length):
        return [random.choice(ColorSequence.COLORS) for _ in range(length)]