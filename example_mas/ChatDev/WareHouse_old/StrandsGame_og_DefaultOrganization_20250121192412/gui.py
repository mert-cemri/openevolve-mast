'''
Contains the StrandsGUI class and related GUI functions.
'''
import tkinter as tk
from game_logic import StrandsGame
class StrandsGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.game = StrandsGame()
        self.create_widgets()
    def create_widgets(self):
        # Create and place GUI widgets
        self.strands_label = tk.Label(self, text="Strands: " + ", ".join(self.game.strands))
        self.strands_label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_combination)
        self.submit_button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        self.completed_label = tk.Label(self, text="Completed Words: None")
        self.completed_label.pack()
    def submit_combination(self):
        # Handle player's submission
        combination = self.entry.get()
        if self.game.check_combination(combination):
            self.result_label.config(text=f"Correct! {combination} is a valid word.")
            self.completed_label.config(text="Completed Words: " + ", ".join(self.game.completed))
        else:
            self.result_label.config(text=f"Incorrect! {combination} is not a valid word.")
        if self.game.is_complete():
            current_text = self.result_label.cget("text")
            self.result_label.config(text=current_text + "\nCongratulations! You've completed the game.")