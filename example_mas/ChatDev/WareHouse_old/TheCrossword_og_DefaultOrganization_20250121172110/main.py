'''
main.py
Contains the CrosswordApp class for managing the GUI and user interactions.
'''
import tkinter as tk
from tkinter import messagebox
from crossword import CrosswordGrid, Clue
class CrosswordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Crossword Puzzle")
        self.grid_size = 10
        self.crossword = CrosswordGrid(self.grid_size)
        self.create_widgets()
    def create_widgets(self):
        self.entries = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=r, column=c)
                self.entries[r][c] = entry
        self.clue_listbox = tk.Listbox(self.master)
        self.clue_listbox.grid(row=self.grid_size, column=0, columnspan=self.grid_size)
        self.word_entry = tk.Entry(self.master)
        self.word_entry.grid(row=self.grid_size + 1, column=0, columnspan=self.grid_size)
        self.submit_button = tk.Button(self.master, text="Submit Word", command=self.submit_word)
        self.submit_button.grid(row=self.grid_size + 2, column=0, columnspan=self.grid_size)
        self.check_button = tk.Button(self.master, text="Check", command=self.check_solution)
        self.check_button.grid(row=self.grid_size + 3, column=0, columnspan=self.grid_size)
        self.add_clues()
    def add_clues(self):
        # Example clues
        clues = [
            Clue(1, "First letter of the alphabet", "A", 0, 0, 'across'),
            Clue(2, "Opposite of down", "UP", 1, 0, 'across'),
            Clue(3, "Not in", "OUT", 0, 0, 'down')
        ]
        for clue in clues:
            self.crossword.add_clue(clue)
            self.clue_listbox.insert(tk.END, f"{clue.number} {clue.direction}: {clue.text}")
    def submit_word(self):
        selected_clue_index = self.clue_listbox.curselection()
        if not selected_clue_index:
            messagebox.showerror("Error", "Please select a clue.")
            return
        selected_clue_index = selected_clue_index[0]
        clue = self.crossword.clues[selected_clue_index]
        word = self.word_entry.get().strip()
        # Validate word length
        if len(word) != len(clue.answer):
            messagebox.showerror("Error", f"Word length does not match the expected length for clue {clue.number} {clue.direction}.")
            return
        if self.crossword.fill_word(clue.number, clue.direction, word):
            self.update_grid()
        else:
            messagebox.showerror("Error", f"Incorrect word for clue {clue.number} {clue.direction}")
    def update_grid(self):
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                self.entries[r][c].delete(0, tk.END)
                self.entries[r][c].insert(0, self.crossword.grid[r][c])
    def check_solution(self):
        if self.crossword.is_complete():
            messagebox.showinfo("Success", "Congratulations! You completed the crossword.")
        else:
            messagebox.showerror("Error", "The crossword is not complete yet.")
def main():
    import os
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Using Xvfb for virtual display.')
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 600))
        display.start()
    root = tk.Tk()
    app = CrosswordApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()