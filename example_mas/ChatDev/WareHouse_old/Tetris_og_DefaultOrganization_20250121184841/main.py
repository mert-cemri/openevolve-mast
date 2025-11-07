'''
Main file to initialize and run the Tetris game.
'''
import pygame
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris')
    game = Game(screen)
    game.run()
if __name__ == '__main__':
    main()