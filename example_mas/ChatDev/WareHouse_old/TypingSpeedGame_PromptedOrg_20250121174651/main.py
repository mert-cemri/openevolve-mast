'''
Main file for the Typing Practice Game. Manages game flow and user interaction.
'''
import time
from word_provider import WordProvider
from timer import Timer
class TypingGame:
    def __init__(self):
        self.word_provider = WordProvider()
        self.timer = Timer()
        self.user_input = ""
        self.displayed_text = ""
    def start_game(self):
        self.displayed_text = self.word_provider.get_random_phrase()
        print(f"Type the following text: {self.displayed_text}")
        self.timer.start_timer()
        self.user_input = input("Your input: ")
        elapsed_time = self.timer.stop_timer()
        wpm = self.calculate_wpm(elapsed_time)
        accuracy = self.calculate_accuracy()
        self.display_results(wpm, accuracy)
    def calculate_wpm(self, elapsed_time):
        words_typed = len(self.user_input.split())
        minutes = elapsed_time / 60
        return words_typed / minutes if minutes > 0 else 0
    def calculate_accuracy(self):
        correct_chars = sum(1 for i, c in enumerate(self.user_input) if i < len(self.displayed_text) and c == self.displayed_text[i])
        total_chars = max(len(self.user_input), len(self.displayed_text))
        return (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    def display_results(self, wpm, accuracy):
        print(f"Words per minute: {wpm:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")
if __name__ == "__main__":
    game = TypingGame()
    game.start_game()