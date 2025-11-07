'''
This module defines the SudokuGUI class, which provides a graphical user interface for the Sudoku puzzle using tkinter.
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver/Creator")
        self.grid = SudokuGrid()
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()
    def create_widgets(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5)
                entry.bind('<FocusOut>', lambda e, r=row, c=col: self.update_grid(r, c))
                self.entries[row][col] = entry
        solve_button = tk.Button(self.master, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)
    def update_grid(self, row, col):
        try:
            value = int(self.entries[row][col].get())
            if 1 <= value <= 9:
                if self.grid.is_valid(row, col, value):
                    self.grid.set_value(row, col, value)
                else:
                    self.entries[row][col].delete(0, tk.END)
                    messagebox.showerror("Invalid Move", "This move violates Sudoku rules.")
            else:
                self.entries[row][col].delete(0, tk.END)
        except ValueError:
            self.entries[row][col].delete(0, tk.END)
    def solve_puzzle(self):
        solver = SudokuSolver(self.grid)
        if solver.solve():
            for row in range(9):
                for col in range(9):
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].insert(0, str(self.grid.grid[row][col]))
        else:
            messagebox.showinfo("No Solution", "No solution exists for the current puzzle.")