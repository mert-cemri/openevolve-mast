'''
Handles user input for entering words into the crossword grid.
'''
from tkinter import Frame, Label, Entry, Button
class WordEntry:
    def __init__(self, master, crossword_grid, clue_manager):
        self.master = master
        self.crossword_grid = crossword_grid
        self.clue_manager = clue_manager
        self.entry_frame = Frame(master)
        self.entry_frame.pack()
        self.clue_label = Label(self.entry_frame, text="Enter word:")
        self.clue_label.pack(side='left')
        self.word_entry = Entry(self.entry_frame)
        self.word_entry.pack(side='left')
        self.submit_button = Button(self.entry_frame, text="Submit", command=self.submit_word)
        self.submit_button.pack(side='left')
    def submit_word(self):
        user_input = self.word_entry.get().upper()
        try:
            clue_number, direction, word = user_input.split()
            clue_number = int(clue_number)
            if direction.lower() not in ['across', 'down']:
                print("Invalid direction. Please enter 'across' or 'down'.")
                return
            start_row, start_col = self.clue_manager.get_start_position(clue_number, direction.lower())
            if start_row is None or start_col is None:
                print("Invalid clue number.")
                return
            if direction.lower() == 'across':
                if start_col + len(word) > len(self.crossword_grid.correct_answers[start_row]):
                    print("Word length does not fit in the grid.")
                    return
            elif direction.lower() == 'down':
                if start_row + len(word) > len(self.crossword_grid.correct_answers):
                    print("Word length does not fit in the grid.")
                    return
            for i, letter in enumerate(word):
                if direction.lower() == 'across':
                    self.crossword_grid.grid_data[start_row][start_col + i] = letter
                else:
                    self.crossword_grid.grid_data[start_row + i][start_col] = letter
            if self.crossword_grid.check_completion():
                print("Congratulations! You completed the crossword.")
        except ValueError:
            print("Invalid input format. Please use 'clue_number direction word'.")