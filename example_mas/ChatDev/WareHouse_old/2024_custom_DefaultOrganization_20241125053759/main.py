'''
Main file to initialize and run the 2048 game with a 10x10 grid.
'''
import pygame
from game import Game
from gui import GUI
def main():
    pygame.init()
    game = Game()
    gui = GUI(game)
    running = True
    while running:
        gui.handle_input()
        gui.update_display()
        if game.is_game_over():
            print("Game Over!")
            running = False
    pygame.quit()
if __name__ == "__main__":
    main()