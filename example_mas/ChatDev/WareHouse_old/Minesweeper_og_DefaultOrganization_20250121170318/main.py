'''
Main entry point for the Minesweeper game application.
'''
from game import MinesweeperGame
from gui import MinesweeperGUI
def main():
    # Initialize the game logic
    game = MinesweeperGame(9, 9, 10)
    # Initialize the GUI
    gui = MinesweeperGUI(game)
    # Start the GUI main loop
    gui.run()
if __name__ == "__main__":
    main()