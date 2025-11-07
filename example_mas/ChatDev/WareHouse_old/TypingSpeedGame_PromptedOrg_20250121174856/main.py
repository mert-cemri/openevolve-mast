'''
Main file to run the typing practice game.
'''
from word_provider import WordProvider
from timer import Timer
class TypingGame:
    def __init__(self):
        self.word_provider = WordProvider()
        self.timer = Timer()
        self.user_input = ""
        self.phrase = ""
        self.elapsed_time = 0
    def start_game(self):
        self.phrase = self.word_provider.get_random_phrase()
        print(f"Type the following phrase: {self.phrase}")
        self.timer.start_timer()
        self.user_input = input("Your input: ")
        self.elapsed_time = self.timer.stop_timer()
        self.display_results()
    def calculate_wpm(self):
        user_words = self.user_input.split()
        total_words = len(user_words)
        minutes = self.elapsed_time / 60
        wpm = total_words / minutes
        return wpm
    def calculate_accuracy(self):
        correct_chars = sum(1 for i, c in enumerate(self.user_input) if i < len(self.phrase) and c == self.phrase[i])
        total_chars = max(len(self.phrase), len(self.user_input))
        accuracy = (correct_chars / total_chars) * 100
        return accuracy
    def display_results(self):
        raw_wpm = self.calculate_wpm()
        accuracy = self.calculate_accuracy()
        adjusted_wpm = raw_wpm * (accuracy / 100)
        print(f"Results:\nRaw Words per minute: {raw_wpm:.2f}\nAdjusted Words per minute: {adjusted_wpm:.2f}\nAccuracy: {accuracy:.2f}%")
if __name__ == "__main__":
    game = TypingGame()
    game.start_game()