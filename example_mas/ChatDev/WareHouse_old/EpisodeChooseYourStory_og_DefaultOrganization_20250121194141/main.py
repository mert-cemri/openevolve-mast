'''
Main module to run the interactive storytelling game.
'''
from gui import GUI
from game import Game
def main():
    gui = GUI()
    game = Game(gui)
    gui.game = game  # Connect GUI to Game
    game.start_game()
    gui.create_main_window()
if __name__ == "__main__":
    main()