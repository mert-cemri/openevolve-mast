'''
This is the main module that initializes and starts the 2048 game.
'''
from game import Game
def main():
    game = Game()
    game.play()
if __name__ == "__main__":
    main()