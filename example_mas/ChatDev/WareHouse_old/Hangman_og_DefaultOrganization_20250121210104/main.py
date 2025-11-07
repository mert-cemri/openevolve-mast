'''
Main application file for the Hangman game using tkinter.
'''
import tkinter as tk
from hangman_game import HangmanGame
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.word_list = ["python", "hangman", "challenge", "programming", "developer"]
        self.game = HangmanGame(self.word_list)
        self.create_widgets()
        self.start_game()
    def create_widgets(self):
        self.display_word_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.display_word_label.pack(pady=20)
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.guess_entry.pack(pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.on_guess)
        self.guess_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)
        self.restart_button = tk.Button(self.root, text="Restart Game", command=self.start_game)
        self.restart_button.pack(pady=10)
        self.restart_button.config(state=tk.DISABLED)  # Initially disabled
    def start_game(self):
        self.game.select_random_word()
        self.update_display()
        self.restart_button.config(state=tk.DISABLED)  # Disable restart button at the start
    def update_display(self):
        self.display_word_label.config(text=self.game.get_display_word())
        self.result_label.config(text="Attempts left: " + str(self.game.attempts_left))
    def on_guess(self):
        letter = self.guess_entry.get().strip().lower()
        if letter:
            message = self.game.guess_letter(letter)
            if message:
                self.result_label.config(text=message)
            else:
                self.update_display()
                if self.game.is_game_over():
                    if all(l in self.game.guessed_letters for l in self.game.word):
                        self.result_label.config(text="Congratulations! You've guessed the word: " + self.game.word)
                    else:
                        self.result_label.config(text="Game Over! The word was: " + self.game.word)
                    self.restart_button.config(state=tk.NORMAL)  # Enable restart button
            self.guess_entry.delete(0, tk.END)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = MainApp()
    app.run()