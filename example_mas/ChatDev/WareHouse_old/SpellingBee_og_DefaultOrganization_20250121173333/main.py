'''
Main application file for the Spelling Bee puzzle game.
'''
from tkinter import Tk
from gui_components import GameUI
from game_logic import SpellingBeeGame
def main():
    root = Tk()
    root.title("Spelling Bee Puzzle")
    game = SpellingBeeGame()
    ui = GameUI(root, game)
    root.mainloop()
if __name__ == "__main__":
    main()