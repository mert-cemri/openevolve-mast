'''
This is the main file that initializes and starts the puzzle game. It coordinates the game flow by interacting with the Game, Puzzle, and UserInterface classes.
'''
from game import Game
def main():
    game = Game()
    game.start()
if __name__ == "__main__":
    main()