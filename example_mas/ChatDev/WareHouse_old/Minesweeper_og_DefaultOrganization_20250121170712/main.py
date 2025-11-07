'''
Main entry point for the Minesweeper game application.
'''
from minesweeper_game import MinesweeperGame
from minesweeper_gui import MinesweeperGUI
def main():
    game = MinesweeperGame()
    gui = MinesweeperGUI(game)
    gui.run()
if __name__ == "__main__":
    main()