'''
Main file to run the Blackjack game with GUI using tkinter.
'''
from blackjack_game import BlackjackGame
from blackjack_gui import BlackjackGUI
def main():
    game = BlackjackGame()
    gui = BlackjackGUI(game)
    gui.run()
if __name__ == "__main__":
    main()