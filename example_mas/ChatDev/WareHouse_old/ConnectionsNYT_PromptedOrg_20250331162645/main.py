'''
This is the main entry point of the puzzle game application. It handles user interaction and game flow.
'''
from game import Game
def main():
    game = Game()
    game.start()
if __name__ == "__main__":
    main()