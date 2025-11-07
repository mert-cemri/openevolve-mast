'''
Main entry point for the Gomoku game application.
'''
from tkinter import Tk
from gomoku_gui import GomokuGUI
def main():
    root = Tk()
    root.title("Gomoku Game")
    gomoku_gui = GomokuGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()