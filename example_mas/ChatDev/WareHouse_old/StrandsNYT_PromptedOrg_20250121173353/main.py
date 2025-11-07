'''
Main script to run the NYT Strands Puzzle game.
'''
from game import Game
def main():
    '''
    Main function to start the game.
    '''
    segments = ["ex", "ample", "word", "another", "word"]
    game = Game(segments)
    game.play()
if __name__ == "__main__":
    main()