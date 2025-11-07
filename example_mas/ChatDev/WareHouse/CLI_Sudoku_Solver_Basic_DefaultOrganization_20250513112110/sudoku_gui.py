'''
Contains the SudokuGUI class to create and manage the graphical user interface for the Sudoku solver.
'''
import tkinter as tk
from sudoku_solver import SudokuSolver
class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.solver = SudokuSolver()
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.window, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.entries[row][col] = entry
        solve_button = tk.Button(self.window, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=0, columnspan=9)
    def update_grid(self, board):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(board[row][col]))
    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                self.board[row][col] = int(value) if value.isdigit() else 0
        if self.solver.solve(self.board):
            self.update_grid(self.board)
        else:
            print("No solution exists")
    def run(self):
        self.window.mainloop()