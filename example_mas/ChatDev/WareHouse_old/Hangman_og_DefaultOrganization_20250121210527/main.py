'''
Main application file for the Hangman game using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from game_logic import HangmanGame
from utils import load_words
class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.word_list = load_words("words.txt")
        self.game = HangmanGame(self.word_list)
        self.label_word = tk.Label(master, text=self.game.get_display_word(), font=("Helvetica", 18))
        self.label_word.pack(pady=20)
        self.entry_letter = tk.Entry(master)
        self.entry_letter.pack(pady=10)
        self.button_guess = tk.Button(master, text="Guess", command=self.guess_letter)
        self.button_guess.pack(pady=10)
        self.label_attempts = tk.Label(master, text=f"Attempts left: {self.game.attempts_left}")
        self.label_attempts.pack(pady=10)
        self.button_new_game = None
        self.start_game()
    def start_game(self):
        if self.button_new_game:
            self.button_new_game.pack_forget()
        self.game.select_random_word()
        self.update_display()
    def guess_letter(self):
        letter = self.entry_letter.get().strip().lower()
        if len(letter) == 1 and letter.isalpha():  # Ensure only a single alphabetic character is processed
            self.game.make_guess(letter)
            self.update_display()
            if self.game.is_game_over():
                self.end_game(self.game.won)
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        self.entry_letter.delete(0, tk.END)
    def update_display(self):
        self.label_word.config(text=self.game.get_display_word())
        self.label_attempts.config(text=f"Attempts left: {self.game.attempts_left}")
    def end_game(self, won):
        if won:
            messagebox.showinfo("Hangman", "Congratulations! You've won!")
        else:
            messagebox.showinfo("Hangman", f"Game Over! The word was: {self.game.word}")
        # Add a button to start a new game
        self.button_new_game = tk.Button(self.master, text="Start New Game", command=self.start_game)
        self.button_new_game.pack(pady=10)
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()