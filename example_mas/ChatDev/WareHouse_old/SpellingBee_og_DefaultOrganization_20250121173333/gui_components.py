'''
GUI components for the Spelling Bee puzzle game.
'''
from tkinter import Frame, Label, Entry, Button, StringVar
class GameUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.word_var = StringVar()
        self.score_var = StringVar(value=f"Score: {self.game.score}")
        self.setup_ui()
    def setup_ui(self):
        frame = Frame(self.master)
        frame.pack(padx=10, pady=10)
        Label(frame, text=f"Central Letter: {self.game.central_letter}").grid(row=0, column=0, columnspan=2)
        Label(frame, text=f"Surrounding Letters: {' '.join(self.game.surrounding_letters)}").grid(row=1, column=0, columnspan=2)
        Entry(frame, textvariable=self.word_var).grid(row=2, column=0)
        Button(frame, text="Submit", command=self.submit_word).grid(row=2, column=1)
        Label(frame, textvariable=self.score_var).grid(row=3, column=0, columnspan=2)
    def submit_word(self):
        word = self.word_var.get().lower()
        if self.game.calculate_score(word):
            self.score_var.set(f"Score: {self.game.score}")
        self.word_var.set("")