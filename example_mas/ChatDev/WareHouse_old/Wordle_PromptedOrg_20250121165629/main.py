'''
This file contains the implementation of a terminal-based Wordle game.
The game allows a player to guess a daily 5-letter word within 6 attempts.
Feedback is provided for each guess, indicating correct letters in the correct position,
correct letters in the wrong position, and incorrect letters.
'''
import random
import os
import hashlib
from datetime import datetime
class WordleGame:
    def __init__(self):
        self.daily_word = self.get_daily_word()
        self.max_attempts = 6
        self.attempts = 0
    def get_daily_word(self):
        # For simplicity, using a fixed list of words. In a real scenario, this could be fetched from a database or API.
        word_list = ['apple', 'grape', 'peach', 'berry', 'melon']
        # Use a hash of the current date to generate a consistent seed
        date_str = datetime.now().strftime("%Y-%m-%d")
        seed = int(hashlib.sha256(date_str.encode()).hexdigest(), 16) % (10 ** 8)
        random.seed(seed)
        return random.choice(word_list)
    def process_guess(self, guess):
        feedback = ['grey'] * 5
        word_letters = list(self.daily_word)
        # First pass: Check for correct letters in the correct position
        for i in range(5):
            if guess[i] == self.daily_word[i]:
                feedback[i] = 'green'
                word_letters[i] = None  # Remove matched letter
        # Second pass: Check for correct letters in the wrong position
        for i in range(5):
            if feedback[i] == 'grey' and guess[i] in word_letters:
                feedback[i] = 'yellow'
                word_letters[word_letters.index(guess[i])] = None  # Remove matched letter
        return feedback
    def display_feedback(self, guess, feedback, use_colors=True):
        colored_output = []
        for i in range(5):
            if feedback[i] == 'green':
                colored_output.append(color_text(guess[i], 'green', use_colors))
            elif feedback[i] == 'yellow':
                colored_output.append(color_text(guess[i], 'yellow', use_colors))
            else:
                colored_output.append(color_text(guess[i], 'grey', use_colors))
        print(' '.join(colored_output))
    def play(self, use_colors=True):
        print("Welcome to Wordle!")
        print("Guess the 5-letter word. You have 6 attempts.")
        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}: ").lower()
            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue
            self.attempts += 1
            feedback = self.process_guess(guess)
            self.display_feedback(guess, feedback, use_colors)
            if guess == self.daily_word:
                print("Congratulations! You've guessed the word!")
                return
        print(f"Sorry, you've used all attempts. The word was: {self.daily_word}")
def supports_color():
    # Check if the terminal supports ANSI colors
    return os.getenv('TERM') in ('xterm-color', 'xterm-256color')
def color_text(text, color, use_colors=True):
    if not use_colors or not supports_color():
        return text
    colors = {
        'green': '\033[92m',  # Green
        'yellow': '\033[93m',  # Yellow
        'grey': '\033[90m',    # Grey
        'end': '\033[0m',      # Reset
    }
    return f"{colors[color]}{text}{colors['end']}"
if __name__ == "__main__":
    game = WordleGame()
    game.play(use_colors=True)  # Set to False if you want to disable colors