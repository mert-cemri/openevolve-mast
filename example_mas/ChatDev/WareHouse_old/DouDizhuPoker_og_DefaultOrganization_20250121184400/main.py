'''
Main entry point for the Dou Dizhu game application.
'''
from game import Game
from gui import GUI
def main():
    game = Game()
    gui = GUI(game)
    gui.setup_gui()
if __name__ == "__main__":
    main()