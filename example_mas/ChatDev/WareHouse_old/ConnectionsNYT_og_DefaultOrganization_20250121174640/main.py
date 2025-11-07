'''
Main entry point for the puzzle game application.
'''
from game import Game
from gui import GUI
def main():
    # Initialize the game logic
    game = Game()
    # Initialize the GUI
    gui = GUI(game)
    # Start the GUI event loop
    gui.start()
if __name__ == "__main__":
    main()