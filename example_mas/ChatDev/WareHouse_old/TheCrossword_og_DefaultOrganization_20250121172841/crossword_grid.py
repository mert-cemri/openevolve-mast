'''
Handles the crossword grid display and validation.
'''
from tkinter import Frame, Entry
class CrosswordGrid:
    def __init__(self, master, clue_manager):
        self.master = master
        self.clue_manager = clue_manager
        self.grid_frame = Frame(master)
        self.grid_frame.pack()
        self.grid_data = [['' for _ in range(5)] for _ in range(5)]  # Example 5x5 grid
        self.correct_answers = [['H', 'E', 'L', 'L', 'O'],
                                ['W', 'O', 'R', 'L', 'D'],
                                ['P', 'Y', 'T', 'H', 'O'],
                                ['N', 'I', 'C', 'E', 'S'],
                                ['C', 'O', 'D', 'E', 'R']]
        self.display_grid()
    def display_grid(self):
        for r in range(5):
            for c in range(5):
                entry = Entry(self.grid_frame, width=2, justify='center')
                entry.grid(row=r, column=c)
                entry.bind("<FocusOut>", lambda e, r=r, c=c: self.validate_word(r, c, e.widget.get()))
    def validate_word(self, row, col, letter):
        if letter.upper() == self.correct_answers[row][col]:
            self.grid_data[row][col] = letter.upper()
        else:
            self.grid_data[row][col] = ''
    def check_completion(self):
        return self.grid_data == self.correct_answers