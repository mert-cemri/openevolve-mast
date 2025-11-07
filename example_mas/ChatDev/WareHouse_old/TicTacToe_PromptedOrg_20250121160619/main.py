'''
Initialize and run the Tic-Tac-Toe game.
'''
import tkinter as tk
from game import Game
from gui import TicTacToeGUI
def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    game = Game()
    gui = TicTacToeGUI(root, game)
    root.mainloop()
if __name__ == "__main__":
    main()