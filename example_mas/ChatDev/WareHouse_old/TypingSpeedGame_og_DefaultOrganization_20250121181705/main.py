'''
Main application file for the Typing Practice Game using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from typing_game import TypingGame, load_word_list
class TypingPracticeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Practice Game")
        self.word_list = load_word_list("words.txt")
        self.game = TypingGame(self.word_list)
        self.label = tk.Label(self.root, text="", font=("Arial", 24))
        self.label.pack(pady=20)
        self.entry = tk.Entry(self.root, font=("Arial", 24))
        self.entry.pack(pady=20)
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=20)
        self.typed_words = []
        self.displayed_words = []  # Initialize list to store displayed words
        self.root.mainloop()
    def start_game(self):
        if hasattr(self, 'start_time'):
            self.root.after_cancel(self.start_time)  # Cancel any existing timer
        self.current_word = self.game.get_random_word()
        self.label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.entry.bind('<Return>', self.check_word)
        self.displayed_words = []  # Reset displayed words for a new game session
        self.typed_words = []  # Reset typed words for a new game session
        self.start_time = self.root.after(60000, self.end_game)  # 60 seconds timer
    def check_word(self, event):
        typed_word = self.entry.get().strip()
        self.typed_words.append(typed_word)
        self.displayed_words.append(self.current_word)  # Store the displayed word
        if typed_word == self.current_word:
            self.current_word = self.game.get_random_word()
            self.label.config(text=self.current_word)
            self.entry.delete(0, tk.END)
    def end_game(self):
        typed_text = ' '.join(self.typed_words)
        displayed_text = ' '.join(self.displayed_words)  # Use displayed words for accuracy
        time_elapsed = 60  # seconds
        wpm = self.game.calculate_wpm(typed_text, time_elapsed)
        accuracy = self.game.calculate_accuracy(typed_text, displayed_text)  # Corrected accuracy calculation
        messagebox.showinfo("Results", f"WPM: {wpm}\nAccuracy: {accuracy}%")
        self.root.after_cancel(self.start_time)
if __name__ == "__main__":
    TypingPracticeApp()