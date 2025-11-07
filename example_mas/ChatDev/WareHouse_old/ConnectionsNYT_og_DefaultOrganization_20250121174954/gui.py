'''
Contains the GUI class which handles the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Word Grouping Puzzle")
        self.word_buttons = []
        self.selected_words = []
        self.create_widgets()
    def create_widgets(self):
        # Create buttons for each word
        for word in self.game.words:
            button = tk.Button(self.root, text=word, command=lambda w=word: self.select_word(w))
            button.pack(side=tk.LEFT)
            self.word_buttons.append(button)
        # Create a submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_guess)
        submit_button.pack(side=tk.BOTTOM)
    def select_word(self, word):
        if word not in self.selected_words:
            self.selected_words.append(word)
        else:
            self.selected_words.remove(word)
    def submit_guess(self):
        if len(self.selected_words) != 4:
            messagebox.showinfo("Invalid Guess", "Please select exactly 4 words.")
            return
        self.game.attempts += 1
        is_correct, correct_words = self.game.check_guess(self.selected_words)
        if is_correct:
            messagebox.showinfo("Correct", "You found a correct group!")
            for button in self.word_buttons:
                if button['text'] in self.selected_words:
                    button.config(state=tk.DISABLED)
            self.selected_words.clear()
        else:
            messagebox.showinfo("Incorrect", f"Try again. Correct words: {', '.join(correct_words)}")
            self.selected_words.clear()
        if self.game.is_game_over():
            if self.game.correct_groups == len(self.game.categories):
                messagebox.showinfo("Game Over", "Congratulations! You found all groups.")
            else:
                messagebox.showinfo("Game Over", "You've run out of attempts.")
            self.root.quit()
    def run(self):
        self.root.mainloop()