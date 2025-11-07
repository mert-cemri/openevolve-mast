'''
This file contains the main entry point of the Gomoku game.
'''
import os
import tkinter as tk
from game import Game
from gomoku_app import GomokuApp
if __name__ == "__main__":
    os.environ["DISPLAY"] = ":0"
    root = tk.Tk()
    app = GomokuApp(root)
    root.mainloop()