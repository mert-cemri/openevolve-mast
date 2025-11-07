'''
Main entry point of the interactive storytelling game.
'''
from game import Game
if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.gui.run()  # Start the GUI loop