'''
Main module to start the Blackjack game.
'''
from blackjack_game import BlackjackGame
def main():
    game = BlackjackGame()
    game.play_round()
if __name__ == "__main__":
    main()