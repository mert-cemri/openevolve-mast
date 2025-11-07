'''
Main entry point for the Blackjack game application.
'''
from blackjack_gui import BlackjackGUI
def main():
    game = BlackjackGUI()
    game.run()
if __name__ == "__main__":
    main()