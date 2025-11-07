'''
Main entry point for the Space Invaders game. Initializes the game and starts the game loop.
'''
import pygame
from game import Game
def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
if __name__ == "__main__":
    main()