'''
Main entry point for the Flappy Bird clone game. Initializes the game and starts the game loop.
'''
import pygame
from game import Game
def main():
    pygame.init()
    game = Game()
    game.run()
if __name__ == "__main__":
    main()