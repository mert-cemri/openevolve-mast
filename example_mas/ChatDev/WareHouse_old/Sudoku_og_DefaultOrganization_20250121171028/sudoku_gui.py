'''
sudoku_gui.py
This module contains the SudokuGUI class which provides the graphical user interface for the Sudoku application.
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
        self.draw_grid()
    def draw_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                entry.bind('<FocusOut>', lambda e, row=i, col=j: self.input_value(row, col, e.widget.get()))
                self.entries[i][j] = entry
        solve_button = tk.Button(self.master, text="Solve", command=self.solve_puzzle)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)
    def input_value(self, row, col, value):
        try:
            value = int(value)
            if 1 <= value <= 9:
                self.grid.set_value(row, col, value)
            else:
                self.entries[row][col].delete(0, tk.END)
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 9.")
        except ValueError:
            self.entries[row][col].delete(0, tk.END)
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
    def check_solution(self):
        if self.grid.is_complete() and self.grid.is_valid():
            messagebox.showinfo("Sudoku", "Congratulations! You solved the puzzle!")
        else:
            messagebox.showwarning("Sudoku", "The solution is not correct.")
    def solve_puzzle(self):
        solver = SudokuSolver(self.grid)
        if solver.solve():
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid.grid[i][j]))
            self.check_solution()
        else:
            messagebox.showwarning("Sudoku", "No solution exists for the given puzzle.")