'''
Provides random words or phrases for the Typing Practice Game.
'''
import random
class WordProvider:
    def __init__(self):
        self.phrases = [
            "hello world", "python programming", "typing practice game", 
            "speed and accuracy", "challenge yourself", "improve your skills",
            "practice makes perfect", "keep typing", "focus on the task",
            "stay motivated"
        ]
    def get_random_phrase(self):
        return random.choice(self.phrases)