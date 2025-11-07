'''
This module contains the HangmanGame class, which manages the game logic, including word selection, tracking guesses, and determining win/loss conditions.
'''
import random
from wordlist import WORDS
class HangmanGame:
    def __init__(self):
        self.word = random.choice(WORDS).upper()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
    def display_word(self):
        displayed_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(displayed_word)
    def get_guess(self):
        guess = input("Enter a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            return self.get_guess()
        return guess
    def update_game_state(self, guess):
        if guess in self.guessed_letters:
            print(f"You've already guessed '{guess}'.")
        elif guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self.guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.incorrect_guesses += 1
            self.guessed_letters.add(guess)
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)
    def is_lost(self):
        return self.incorrect_guesses >= self.max_incorrect_guesses
    def start(self):
        print("Welcome to Hangman!")
        while not self.is_won() and not self.is_lost():
            self.display_word()
            guess = self.get_guess()
            self.update_game_state(guess)
            print(f"Incorrect guesses: {self.incorrect_guesses}/{self.max_incorrect_guesses}")
        if self.is_won():
            print(f"Congratulations! You've guessed the word: {self.word}")
        else:
            print(f"Game over! The word was: {self.word}")