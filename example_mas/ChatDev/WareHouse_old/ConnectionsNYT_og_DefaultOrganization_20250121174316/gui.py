'''
This module contains the GameGUI class, which manages the graphical user interface for the word categorization puzzle.
'''
import tkinter as tk
from tkinter import messagebox
import os
class GameGUI:
    def __init__(self, game):
        # Check if the DISPLAY environment variable is set
        if not os.environ.get('DISPLAY'):
            os.environ['DISPLAY'] = ':99'  # Set a default display to a virtual display
        self.game = game
        self.root = tk.Tk()
        self.root.title("Word Categorization Puzzle")
        self.selected_words = []
        # Create buttons for each word
        self.buttons = {}
        for word in self.game.words:
            button = tk.Button(self.root, text=word, command=lambda w=word: self.select_word(w))
            button.pack(side=tk.LEFT, padx=5, pady=5)
            self.buttons[word] = button
        # Create a submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_group)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)
    def select_word(self, word):
        # Select or deselect a word
        if word in self.selected_words:
            self.selected_words.remove(word)
            self.buttons[word].config(relief=tk.RAISED)
        else:
            self.selected_words.append(word)
            self.buttons[word].config(relief=tk.SUNKEN)
    def submit_group(self):
        # Submit the selected group of words
        if len(self.selected_words) != 4:
            messagebox.showwarning("Invalid Selection", "Please select exactly 4 words.")
            return
        is_valid, category = self.game.check_group(self.selected_words)
        if is_valid:
            messagebox.showinfo("Correct!", f"You found a correct group: {category}")
            for word in self.selected_words:
                self.buttons[word].config(state=tk.DISABLED)
        else:
            messagebox.showerror("Incorrect", "The selected words do not form a valid group.")
        self.selected_words.clear()
        self.game.increment_tries()
        if self.game.is_game_over():
            if len(self.game.correct_groups) == len(self.game.categories):
                messagebox.showinfo("Game Over", "Congratulations! You found all the groups.")
            else:
                messagebox.showinfo("Game Over", "You've run out of tries. Better luck next time!")
            self.root.quit()
    def run(self):
        # Run the GUI main loop
        self.root.mainloop()