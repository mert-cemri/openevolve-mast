'''
Contains the GUI class which manages the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Word Grouping Puzzle")
        self.selected_words = []
        self.buttons = {}
        # Create buttons for each word
        for word in self.game.words:
            button = tk.Button(self.root, text=word, command=lambda w=word: self.select_word(w))
            button.pack(side=tk.LEFT)
            self.buttons[word] = button
        self.check_button = tk.Button(self.root, text="Check Group", command=self.on_guess)
        self.check_button.pack(side=tk.BOTTOM)
        self.status_label = tk.Label(self.root, text="Select four words to form a group.")
        self.status_label.pack(side=tk.BOTTOM)
    def select_word(self, word):
        if word in self.selected_words:
            self.selected_words.remove(word)
            self.buttons[word].config(relief=tk.RAISED)
        else:
            if len(self.selected_words) < 4:
                self.selected_words.append(word)
                self.buttons[word].config(relief=tk.SUNKEN)
        self.update_display()
    def update_display(self):
        self.status_label.config(text=f"Selected words: {', '.join(self.selected_words)}")
    def on_guess(self):
        if len(self.selected_words) != 4:
            messagebox.showinfo("Invalid Selection", "Please select exactly four words.")
            return
        is_correct, message = self.game.check_guess(self.selected_words)
        messagebox.showinfo("Result", message)
        if is_correct:
            for word in self.selected_words:
                self.buttons[word].config(state=tk.DISABLED)
        self.selected_words.clear()
        self.update_display()
        if self.game.is_game_over():
            self.end_game()
    def end_game(self):
        if len(self.game.correct_groups) == len(self.game.categories):
            messagebox.showinfo("Game Over", "Congratulations! You've found all categories.")
        else:
            messagebox.showinfo("Game Over", "Game over! You've run out of tries.")
        self.root.quit()
    def start(self):
        self.root.mainloop()