'''
Provides random words or phrases for the typing game.
'''
import random
class WordProvider:
    def __init__(self):
        self.phrases = [
            "The quick brown fox jumps over the lazy dog",
            "Hello world",
            "Python programming is fun",
            "Practice makes perfect",
            "Stay hungry stay foolish"
        ]
    def get_random_phrase(self):
        return random.choice(self.phrases)