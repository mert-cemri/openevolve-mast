'''
This script implements a command-line Wordle game where the player has six attempts to guess a five-letter word. Feedback is provided for each guess, indicating correct letters in the correct position (green), correct letters in the wrong position (yellow), and incorrect letters (grey). The feedback is color-coded for better visual representation in the terminal.
'''
import random
from colorama import Fore, Style
class WordleGame:
    def __init__(self, word_list):
        self.target_word = random.choice(word_list).upper()
        self.max_attempts = 6
        self.attempts = 0
    def check_guess(self, guess):
        guess = guess.upper()
        feedback = ['grey'] * 5
        target_word_list = list(self.target_word)
        # First pass: check for correct letters in the correct position
        for i in range(5):
            if guess[i] == self.target_word[i]:
                feedback[i] = Fore.GREEN + guess[i] + Style.RESET_ALL
                target_word_list[i] = None  # Mark this letter as used
        # Second pass: check for correct letters in the wrong position
        for i in range(5):
            if feedback[i] == 'grey' and guess[i] in target_word_list:
                feedback[i] = Fore.YELLOW + guess[i] + Style.RESET_ALL
                target_word_list[target_word_list.index(guess[i])] = None  # Mark this letter as used
            elif feedback[i] == 'grey':
                feedback[i] = Fore.LIGHTBLACK_EX + guess[i] + Style.RESET_ALL
        return feedback
    def is_game_over(self, guess):
        self.attempts += 1
        return guess.upper() == self.target_word or self.attempts >= self.max_attempts
    def reveal_solution(self):
        return self.target_word
def main():
    word_list = ['apple', 'berry', 'cherry', 'mango', 'peach', 'grape', 'lemon']
    game = WordleGame(word_list)
    print("Welcome to Wordle!")
    print("You have 6 attempts to guess the 5-letter word.")
    while True:
        guess = input("Enter your guess: ").strip()
        if len(guess) != 5 or not guess.isalpha():
            print("Please enter a valid 5-letter word.")
            continue
        feedback = game.check_guess(guess)
        print("Feedback:", ''.join(feedback))
        if game.is_game_over(guess):
            if guess.upper() == game.reveal_solution():
                print("Congratulations! You've guessed the word!")
            else:
                print(f"Game Over! The correct word was: {game.reveal_solution()}")
            break
if __name__ == "__main__":
    main()