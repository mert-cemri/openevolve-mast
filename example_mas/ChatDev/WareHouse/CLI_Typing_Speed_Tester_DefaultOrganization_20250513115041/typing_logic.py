'''
Handles the typing logic, including timing, WPM calculation, and accuracy.
'''
import time
class TypingTest:
    def __init__(self, paragraph):
        self.paragraph = paragraph
        self.start_time = None
        self.typed_text = ""
        self.is_running = False
    def start(self):
        self.start_time = time.time()
        self.is_running = True
        self.typed_text = ""
    def stop(self):
        self.is_running = False
    def update_typed_text(self, text):
        self.typed_text = text
    def is_complete(self):
        return self.typed_text == self.paragraph
    def calculate_results(self):
        elapsed_time = time.time() - self.start_time
        words_typed = len(self.typed_text.split())
        wpm = (words_typed / elapsed_time) * 60
        correct_chars = sum(1 for i, c in enumerate(self.typed_text) if i < len(self.paragraph) and c == self.paragraph[i])
        accuracy = (correct_chars / len(self.paragraph)) * 100 if self.paragraph else 0
        return round(wpm, 2), round(accuracy, 2)