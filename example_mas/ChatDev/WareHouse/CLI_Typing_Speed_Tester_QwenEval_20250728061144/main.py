'''
Main entry point for the Typing Speed Tester application.
Handles the overall flow of the application, including displaying the paragraph,
capturing user input, and calculating WPM and accuracy.
'''
import sys
import time
from paragraph_generator import ParagraphGenerator
from timer import Timer
from utils import calculate_wpm, calculate_accuracy
class TypingSpeedTester:
    def __init__(self):
        self.paragraph_generator = ParagraphGenerator()
        self.timer = Timer()
    def run(self):
        print("Welcome to the Typing Speed Tester!")
        while True:
            input("Press Enter to start the test...")
            self.start_test()
            retry = input("Do you want to try again? (y/n): ").strip().lower()
            if retry != 'y':
                break
    def start_test(self):
        paragraph = self.paragraph_generator.generate_paragraph()
        print("\nType the following paragraph:\n")
        print(paragraph)
        print("\n")
        self.timer.start()
        user_input = input()
        self.timer.stop()
        wpm = calculate_wpm(user_input, self.timer.elapsed_time)
        accuracy = calculate_accuracy(user_input, paragraph)
        print(f"\nTime taken: {self.timer.elapsed_time:.2f} seconds")
        print(f"Words per minute (WPM): {wpm:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")
        self.provide_feedback(user_input, paragraph)
    def provide_feedback(self, user_input, paragraph):
        user_words = user_input.split()
        paragraph_words = paragraph.split()
        if len(user_words) > len(paragraph_words):
            print("You typed more words than the paragraph. Please focus on accuracy.")
        elif len(user_words) < len(paragraph_words):
            print("You typed fewer words than the paragraph. Please try to complete the paragraph.")
        else:
            print("Great job on completing the paragraph!")
if __name__ == "__main__":
    tester = TypingSpeedTester()
    tester.run()