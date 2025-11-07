'''
Main entry point for the Checkers game. Initializes the game and starts the game loop.
'''
from checkers_game import CheckersGame
def main():
    game = CheckersGame()
    while not game.check_winner():
        game.play_turn()
        game.switch_player()
if __name__ == "__main__":
    main()