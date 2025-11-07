'''
Main application file for the Typing Practice Game. It initializes the GUI, manages the game flow, and calculates results.
'''
import tkinter as tk
import random
import time
import os
class TypingPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Practice Game")
        # Initialize variables
        self.words = ["hello", "world", "python", "programming", "typing", "practice", "speed", "accuracy"]
        self.current_word = ""
        self.start_time = None
        self.typed_words = []
        # Setup GUI components
        self.setup_gui()
    def setup_gui(self):
        # Word display
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)
        # Entry box for user input
        self.entry = tk.Entry(self.root, font=("Helvetica", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_input)
        # Start button
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=20)
        # Result display
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.result_label.pack(pady=20)
    def start_game(self):
        self.start_time = time.time()
        self.typed_words = []
        self.next_word()
        self.check_time()  # Start the timer
    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
    def check_input(self, event):
        # Process the typed word
        typed_word = self.entry.get().strip()
        self.typed_words.append((self.current_word, typed_word))
        self.next_word()
    def check_time(self):
        if time.time() - self.start_time > 60:
            self.end_game()
        else:
            self.root.after(1000, self.check_time)  # Check every second
    def end_game(self):
        self.entry.unbind("<Return>")
        self.entry.config(state='disabled')
        wpm, accuracy = self.calculate_results()
        self.result_label.config(text=f"WPM: {wpm}, Accuracy: {accuracy}%")
    def calculate_results(self):
        correct_words = sum(1 for actual, typed in self.typed_words if actual == typed)
        total_time_minutes = (time.time() - self.start_time) / 60
        wpm = correct_words / total_time_minutes if total_time_minutes > 0 else 0
        accuracy = (correct_words / len(self.typed_words)) * 100 if len(self.typed_words) > 0 else 0
        return wpm, accuracy
if __name__ == "__main__":
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        print("Error: No display found. Please ensure you are running in an environment with a graphical display.")
    else:
        root = tk.Tk()
        app = TypingPracticeApp(root)
        root.mainloop()