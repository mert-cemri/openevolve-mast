'''
This is the main file for the typing practice game. It initializes the game and handles the GUI.
'''
import tkinter as tk
import random
import time
from utils import load_words, calculate_wpm, calculate_accuracy
class TypingGame:
    def __init__(self, master, duration=60):
        self.master = master
        self.master.title("Typing Practice Game")
        self.words = load_words()
        self.current_word = ""
        self.start_time = 0
        self.typed_words = []
        self.correct_words = 0
        self.duration = duration  # Duration in seconds
        self.label = tk.Label(master, text="", font=("Helvetica", 24))
        self.label.pack(pady=20)
        self.entry = tk.Entry(master, font=("Helvetica", 24))
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_input)
        self.result_label = tk.Label(master, text="", font=("Helvetica", 18))
        self.result_label.pack(pady=20)
        self.start_game()
    def start_game(self):
        self.start_time = time.time()
        self.display_word()
        self.master.after(1000, self.check_time)  # Check time every second
    def display_word(self):
        self.current_word = random.choice(self.words)
        self.label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
    def check_input(self, event):
        typed_word = self.entry.get().strip()
        self.typed_words.append(typed_word)
        if typed_word == self.current_word:
            self.correct_words += 1
        self.display_word()
    def check_time(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.duration:
            self.calculate_results()
        else:
            self.master.after(1000, self.check_time)
    def calculate_results(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        wpm = calculate_wpm(self.correct_words, elapsed_time)
        accuracy = calculate_accuracy(self.typed_words, self.correct_words)
        self.result_label.config(text=f"WPM: {wpm}, Accuracy: {accuracy}%")
        self.entry.config(state='disabled')  # Disable entry after game ends
if __name__ == "__main__":
    try:
        root = tk.Tk()
        game = TypingGame(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display environment available.")
        print(e)