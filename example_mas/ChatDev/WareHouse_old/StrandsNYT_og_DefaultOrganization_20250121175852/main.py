'''
Main entry point for the NYT Strands puzzle application.
'''
from game import Game
from gui import GUI
def main():
    game = Game()
    gui = GUI(game)
    gui.run()
if __name__ == "__main__":
    main()