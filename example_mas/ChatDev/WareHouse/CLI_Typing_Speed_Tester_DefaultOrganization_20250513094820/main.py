'''
Main entry point for the CLI typing speed tester application.
'''
import random
import time
class TypingSpeedTester:
    def __init__(self):
        self.start_time = None
        self.paragraph = self.get_random_paragraph()
    def get_random_paragraph(self):
        paragraphs = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a great programming language for beginners.",
            "Typing speed tests are a fun way to improve your typing skills."
        ]
        return random.choice(paragraphs)
    def start_test(self):
        self.start_time = time.time()
        print("Type the following paragraph:")
        print(self.paragraph)
        user_input = input("\nYour input: ")
        self.end_test(user_input)
    def end_test(self, user_input):
        end_time = time.time()
        time_taken = end_time - self.start_time
        wpm = self.calculate_wpm(user_input, time_taken)
        accuracy = self.calculate_accuracy(user_input)
        print(f"\nResults:\nWPM: {wpm}\nAccuracy: {accuracy}%")
    def calculate_wpm(self, user_input, time_taken):
        words_typed = len(user_input.split())
        minutes = time_taken / 60
        wpm = words_typed / minutes
        return round(wpm, 2)
    def calculate_accuracy(self, user_input):
        correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(self.paragraph) and c == self.paragraph[i])
        total_chars = len(self.paragraph)
        accuracy = (correct_chars / total_chars) * 100
        return round(accuracy, 2)
if __name__ == "__main__":
    tester = TypingSpeedTester()
    tester.start_test()