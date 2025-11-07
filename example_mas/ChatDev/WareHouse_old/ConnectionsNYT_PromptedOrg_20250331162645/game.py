'''
This module contains the Game class, which manages the overall game state, including the grid of words, the categories, and the player's progress.
'''
from wordgrid import WordGrid
from category import Category
from puzzlegenerator import PuzzleGenerator
from feedback import Feedback
class Game:
    def __init__(self):
        self.word_grid = WordGrid()
        self.categories = []
        self.feedback = Feedback()
        self.mistakes = 0
        self.max_mistakes = 4
        self.puzzle_generator = PuzzleGenerator()
    def start(self):
        self.categories, self.word_grid.words = self.puzzle_generator.generate_puzzle()
        self.word_grid.shuffle()
        self.play()
    def play(self):
        while self.mistakes < self.max_mistakes and self.word_grid.words:
            self.word_grid.display()
            guess = self.get_player_guess()
            if self.is_correct_guess(guess):
                self.feedback.correct_guess()
                self.remove_correct_words(guess)
            else:
                self.feedback.incorrect_guess()
                self.mistakes += 1
        self.end_game()
    def get_player_guess(self):
        while True:
            try:
                guess = input("Enter your guess (four words separated by spaces): ").strip().split()
                if len(guess) != 4:
                    raise ValueError("You must enter exactly four words.")
                if not all(word in self.word_grid.words for word in guess):
                    raise ValueError("All words must be from the current grid.")
                return guess
            except ValueError as e:
                print(e)
    def is_correct_guess(self, guess):
        return any(set(guess) == set(category.words) for category in self.categories)
    def remove_correct_words(self, guess):
        self.word_grid.remove_words(guess)
    def end_game(self):
        if not self.word_grid.words:
            print("Congratulations! You've solved the puzzle.")
        else:
            print("Game over. Better luck next time!")