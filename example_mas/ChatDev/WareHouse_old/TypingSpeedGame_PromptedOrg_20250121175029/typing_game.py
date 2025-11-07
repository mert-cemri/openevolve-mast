'''
TypingGame class to manage the typing practice game flow.
'''
import time
from phrase_provider import PhraseProvider
from timer import Timer
class TypingGame:
    def __init__(self):
        self.phrase_provider = PhraseProvider()
        self.timer = Timer()
        self.current_phrase = ""
        self.user_input = ""
    def start_game(self):
        print("Welcome to the Typing Practice Game!")
        self.current_phrase = self.phrase_provider.get_random_phrase()
        print(f"Type the following phrase: {self.current_phrase}")
        self.timer.start()
        self.user_input = input("Your input: ")
        elapsed_time = self.timer.stop()
        wpm = self.calculate_wpm(elapsed_time)
        accuracy = self.calculate_accuracy()
        self.end_game(wpm, accuracy)
    def calculate_wpm(self, elapsed_time):
        correct_words = sum(1 for i, word in enumerate(self.user_input.split()) 
                            if i < len(self.current_phrase.split()) and word == self.current_phrase.split()[i])
        minutes = elapsed_time / 60
        wpm = correct_words / minutes
        return wpm
    def calculate_accuracy(self):
        correct_chars = sum(1 for i, c in enumerate(self.user_input) if i < len(self.current_phrase) and c == self.current_phrase[i])
        total_chars = len(self.current_phrase)
        accuracy = (correct_chars / total_chars) * 100
        return accuracy
    def end_game(self, wpm, accuracy):
        print(f"Words per minute: {wpm:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")