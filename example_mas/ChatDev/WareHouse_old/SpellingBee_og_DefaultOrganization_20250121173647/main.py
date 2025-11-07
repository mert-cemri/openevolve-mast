'''
Main application file for the Spelling Bee puzzle game.
'''
import tkinter as tk
from game_logic import SpellingBeeGame
class SpellingBeeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Spelling Bee Puzzle")
        self.central_letter = 'a'
        self.other_letters = ['b', 'c', 'd', 'e', 'f', 'g']
        self.game = SpellingBeeGame(self.central_letter, self.other_letters)
        self.score = 0
        self.create_widgets()
    def create_widgets(self):
        instructions = (
            "Form words using the letters provided.\n"
            "Each word must include the central letter.\n"
            "Words must be at least 4 letters long.\n"
            "Use all 7 letters for a bonus!"
        )
        self.instructions_label = tk.Label(self.root, text=instructions)
        self.instructions_label.pack()
        self.letters_label = tk.Label(self.root, text=f"Letters: {self.central_letter} {' '.join(self.other_letters)}")
        self.letters_label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_word)
        self.submit_button.pack()
        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack()
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}")
        self.score_label.pack()
    def submit_word(self):
        word = self.entry.get().strip().lower()
        if self.game.is_valid_word(word):
            word_score = self.game.calculate_score(word)
            self.score += word_score
            is_bonus = len(set(word)) == 7
            self.update_feedback(f"Good job! '{word}' is worth {word_score} points.", is_bonus)
        else:
            self.update_feedback(f"'{word}' is not a valid word.")
        self.entry.delete(0, tk.END)
        self.score_label.config(text=f"Score: {self.score}")
    def update_feedback(self, message, is_bonus=False):
        if is_bonus:
            message += " Bonus for using all letters!"
        self.feedback_label.config(text=message)
    def start_game(self):
        self.root.mainloop()
if __name__ == "__main__":
    try:
        app = SpellingBeeApp()
        app.start_game()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display environment available.")
        print(e)