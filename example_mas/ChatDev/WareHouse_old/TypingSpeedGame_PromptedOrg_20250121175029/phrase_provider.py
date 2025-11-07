'''
PhraseProvider class to supply random phrases for the typing game.
'''
import random
class PhraseProvider:
    def __init__(self):
        self.phrases = [
            "The quick brown fox jumps over the lazy dog",
            "A journey of a thousand miles begins with a single step",
            "To be or not to be, that is the question",
            "All that glitters is not gold",
            "The only thing we have to fear is fear itself"
        ]
    def get_random_phrase(self):
        return random.choice(self.phrases)