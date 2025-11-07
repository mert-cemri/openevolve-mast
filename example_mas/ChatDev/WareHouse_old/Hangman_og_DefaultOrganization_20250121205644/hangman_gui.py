'''
Contains the HangmanGUI class which manages the graphical user interface.
'''
import tkinter as tk
from hangman_game import HangmanGame
class HangmanGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.word_list = ["PYTHON", "DEVELOPER", "PROGRAMMING", "HANGMAN", "COMPUTER"]
        self.game = HangmanGame(self.word_list)
        self.display_word_label = tk.Label(self.root, text=self.game.get_display_word(), font=("Helvetica", 18))
        self.display_word_label.pack(pady=20)
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.guess_entry.pack(pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.handle_guess)
        self.guess_button.pack(pady=10)
        self.incorrect_guesses_label = tk.Label(self.root, text="Incorrect guesses: ", font=("Helvetica", 14))
        self.incorrect_guesses_label.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)
    def run(self):
        self.root.mainloop()
    def update_display(self):
        self.display_word_label.config(text=self.game.get_display_word())
        self.incorrect_guesses_label.config(text=f"Incorrect guesses: {self.game.get_incorrect_guesses()}")
    def handle_guess(self):
        guess = self.guess_entry.get().strip()
        if len(guess) == 1 and guess.isalpha():
            self.game.guess_letter(guess)
            self.update_display()
            self.guess_entry.delete(0, tk.END)
            if self.game.is_game_over():
                self.show_result()
    def show_result(self):
        if self.game.is_winner():
            self.result_label.config(text="Congratulations! You won!")
        else:
            self.result_label.config(text=f"Game Over! The word was {self.game.secret_word}.")
        self.guess_button.config(state=tk.DISABLED)