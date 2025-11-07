'''
Main module to run the Sudoku application with GUI.
'''
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver
from sudoku_gui import SudokuGUI
import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Sudoku Solver/Creator")
    sudoku_gui = SudokuGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()