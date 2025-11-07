'''
This is the main script to run the Sudoku Solver/Creator application.
'''
import tkinter as tk
from sudoku_gui import SudokuGUI
def main():
    try:
        root = tk.Tk()
        app = SudokuGUI(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display environment. Details:", e)
if __name__ == "__main__":
    main()