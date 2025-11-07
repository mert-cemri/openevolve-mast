'''
Main entry point for the Gomoku application.
'''
import tkinter as tk
from gui import GomokuGUI
def main():
    root = tk.Tk()
    app = GomokuGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()