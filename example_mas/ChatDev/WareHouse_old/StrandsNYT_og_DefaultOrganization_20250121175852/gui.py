'''
Graphical User Interface for the NYT Strands puzzle using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("NYT Strands Puzzle")
        self.create_widgets()
    def create_widgets(self):
        self.buttons = []
        for segment in self.game.segments:
            button = tk.Button(self.root, text=segment.text, command=lambda s=segment: self.on_segment_click(s))
            button.pack(side=tk.LEFT)
            self.buttons.append(button)
        self.check_button = tk.Button(self.root, text="Check", command=self.check_solution)
        self.check_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(side=tk.LEFT)
    def on_segment_click(self, segment):
        if segment.is_selected:
            segment.is_selected = False
            self.game.selected_segments.remove(segment)
        else:
            segment.is_selected = True
            self.game.selected_segments.append(segment)
        self.update_display()
    def update_display(self):
        for button, segment in zip(self.buttons, self.game.segments):
            button.config(relief=tk.SUNKEN if segment.is_selected else tk.RAISED)
    def check_solution(self):
        if self.game.check_solution():
            self.show_message("Correct!", "Congratulations, you formed a valid word!")
        else:
            self.show_message("Incorrect", "Try again.")
    def reset_game(self):
        self.game.reset_game()
        self.update_display()
    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    def run(self):
        self.root.mainloop()