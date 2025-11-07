'''
Main file to run the Flappy Bird game.
'''
import pygame
from game import Game
def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Flappy Bird Clone")
    clock = pygame.time.Clock()
    game = Game(screen, clock)
    game.run()
if __name__ == "__main__":
    main()