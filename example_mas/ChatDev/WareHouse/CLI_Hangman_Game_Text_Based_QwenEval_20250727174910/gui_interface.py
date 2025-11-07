'''
Module to handle user input and display the game state for the GUI version using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from hangman_game import HangmanGame
class GUIInterface:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Hangman")
        self.root.geometry("400x200")
        self.display_word_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.display_word_label.pack(pady=20)
        self.incorrect_guesses_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.incorrect_guesses_label.pack()
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.guess_entry.pack(pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", font=("Helvetica", 14), command=self.guess)
        self.guess_button.pack()
        self.update_display()
    def run(self):
        self.root.mainloop()
    def update_display(self):
        self.display_word_label.config(text=self.game.get_display_word())
        self.incorrect_guesses_label.config(text=f"Incorrect guesses: {self.game.incorrect_guesses}/{self.game.max_incorrect_guesses}")
    def guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        result = self.game.guess_letter(guess)
        messagebox.showinfo("Result", result)
        self.update_display()
        if self.game.is_game_over():
            if self.game.is_game_won():
                messagebox.showinfo("Congratulations", f"You guessed the word: {self.game.word}")
            else:
                messagebox.showinfo("Game Over", f"Game over! You failed to guess the word: {self.game.word}")
            self.root.quit()