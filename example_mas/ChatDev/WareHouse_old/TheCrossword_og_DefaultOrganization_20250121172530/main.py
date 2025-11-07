'''
Main application file for the crossword puzzle GUI.
'''
import tkinter as tk
from crossword import CrosswordGrid, Clue
class CrosswordApp:
    def __init__(self, master, rows=5, cols=5, clues=None):
        self.master = master
        self.master.title("Crossword Puzzle")
        # Initialize crossword grid and clues
        self.grid = CrosswordGrid(rows, cols, clues)
        self.clues = clues if clues else [
            Clue(1, 'across', 'First letter of the alphabet', 'A', 0, 0),
            Clue(2, 'down', 'Opposite of yes', 'NO', 0, 1)
        ]
        self.create_widgets()
    def create_widgets(self):
        # Create and arrange GUI widgets
        self.entries = {}
        for i in range(self.grid.rows):
            for j in range(self.grid.cols):
                var = tk.StringVar()
                var.trace("w", lambda name, index, mode, var=var, i=i, j=j: self.validate_entry(var, i, j))
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), textvariable=var)
                entry.grid(row=i, column=j)
                self.entries[(i, j)] = var
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_word)
        self.submit_button.grid(row=self.grid.rows, column=0, columnspan=self.grid.cols)
        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=self.grid.rows + 1, column=0, columnspan=self.grid.cols)
    def validate_entry(self, var, i, j):
        letter = var.get().upper()
        if len(letter) > 1 or not letter.isalpha():
            var.set('')  # Clear invalid input
    def submit_word(self):
        # Collect words from entries and validate
        for clue in self.clues:
            word = ""
            if clue.direction == 'across':
                for j in range(len(clue.answer)):
                    word += self.entries[(clue.start_row, clue.start_col + j)].get().upper()
            elif clue.direction == 'down':
                for i in range(len(clue.answer)):
                    word += self.entries[(clue.start_row + i, clue.start_col)].get().upper()
            if not self.grid.validate_word(clue, word):
                self.status_label.config(text=f"Incorrect word for clue {clue.number} {clue.direction}")
                return
        if self.grid.is_complete():
            self.status_label.config(text="Congratulations! Crossword complete.")
        else:
            self.status_label.config(text="Keep going!")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CrosswordApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you are running this on a system with a graphical display.")
        print(e)