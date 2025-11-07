'''
Module to create the Sudoku GUI using tkinter.
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.grid = SudokuGrid()
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.entries[row][col] = entry
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9)
    def check_solution(self):
        for row in range(9):
            for col in range(9):
                try:
                    num = int(self.entries[row][col].get())
                    self.grid.grid[row][col] = num
                except ValueError:
                    messagebox.showerror("Input Error", "Invalid input detected. Please enter numbers between 1 and 9.")
                    return False
        if self.grid.is_grid_valid():
            messagebox.showinfo("Success", "Congratulations! The solution is correct.")
        else:
            messagebox.showwarning("Incorrect", "The solution is incorrect. Please try again.")
    def solve_puzzle(self):
        for row in range(9):
            for col in range(9):
                try:
                    num = int(self.entries[row][col].get())
                    self.grid.grid[row][col] = num
                except ValueError:
                    self.grid.grid[row][col] = 0
        solver = SudokuSolver(self.grid)
        if solver.solve():
            for row in range(9):
                for col in range(9):
                    self.entries[row][col].delete(0, tk.END)
                    self.entries[row][col].insert(0, str(self.grid.grid[row][col]))
        else:
            messagebox.showerror("No Solution", "No solution exists")