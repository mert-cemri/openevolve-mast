'''
Game logic for the Typing Practice Game.
'''
import random
class TypingGame:
    def __init__(self, word_list):
        self.word_list = word_list
    def get_random_word(self):
        return random.choice(self.word_list)
    def calculate_wpm(self, typed_text, time_elapsed):
        words_typed = len(typed_text.split())
        return (words_typed / time_elapsed) * 60
    def calculate_accuracy(self, typed_text, target_text):
        typed_words = typed_text.split()
        target_words = target_text.split()
        correct_words = sum(1 for tw, twt in zip(typed_words, target_words) if tw == twt)
        return (correct_words / len(target_words)) * 100 if target_words else 0
def load_word_list(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]