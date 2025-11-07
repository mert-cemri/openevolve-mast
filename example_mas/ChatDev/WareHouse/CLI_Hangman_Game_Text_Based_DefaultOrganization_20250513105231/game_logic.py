'''
Game logic for the Hangman game, including word selection and guess handling.
'''
import random
class HangmanGame:
    def __init__(self):
        self.words = ["python", "hangman", "challenge", "programming", "developer"]
        self.word = random.choice(self.words)
        self.guessed_letters = set()
        self.incorrect_guesses = []
        self.max_incorrect = 6
    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    def guess_letter(self, letter):
        if letter in self.word:
            self.guessed_letters.add(letter)
        else:
            if letter not in self.incorrect_guesses:
                self.incorrect_guesses.append(letter)
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)
    def is_lost(self):
        return len(self.incorrect_guesses) >= self.max_incorrect