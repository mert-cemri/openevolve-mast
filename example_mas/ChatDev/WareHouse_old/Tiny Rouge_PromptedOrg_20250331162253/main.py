'''
Main entry point for the roguelike game. Manages the game loop and user input.
'''
from game import Game
def main():
    game = Game()
    game.run()
if __name__ == "__main__":
    main()