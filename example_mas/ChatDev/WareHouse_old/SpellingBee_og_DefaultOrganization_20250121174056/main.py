'''
Main application file for the Spelling Bee puzzle game.
'''
import tkinter as tk
from game_logic import SpellingBeeGame
class SpellingBeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spelling Bee Puzzle")
        self.game = SpellingBeeGame()
        self.central_letter = tk.StringVar(value=self.game.central_letter)
        self.surrounding_letters = tk.StringVar(value=' '.join(self.game.surrounding_letters))
        self.user_input = tk.StringVar()
        self.feedback = tk.StringVar()
        self.score = tk.IntVar(value=0)
        self.setup_gui()
    def setup_gui(self):
        tk.Label(self.root, text="Central Letter:").pack()
        tk.Label(self.root, textvariable=self.central_letter).pack()
        tk.Label(self.root, text="Surrounding Letters:").pack()
        tk.Label(self.root, textvariable=self.surrounding_letters).pack()
        tk.Entry(self.root, textvariable=self.user_input).pack()
        tk.Button(self.root, text="Submit", command=self.submit_word).pack()
        tk.Label(self.root, text="Feedback:").pack()
        tk.Label(self.root, textvariable=self.feedback).pack()
        tk.Label(self.root, text="Score:").pack()
        tk.Label(self.root, textvariable=self.score).pack()
    def submit_word(self):
        word = self.user_input.get().strip().lower()
        if self.game.is_valid_word(word):
            self.score.set(self.score.get() + self.game.calculate_score(word))
            self.feedback.set("Good job!")
        else:
            self.feedback.set("Invalid word.")
        self.user_input.set("")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = SpellingBeeApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display available.")
        print(e)