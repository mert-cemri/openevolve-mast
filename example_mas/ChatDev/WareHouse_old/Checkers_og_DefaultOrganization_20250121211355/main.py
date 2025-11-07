'''
Main entry point for the Checkers game application.
'''
import pygame
from game import Game
from gui import GUI
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Checkers Game')
    game = Game()
    gui = GUI(screen, game)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gui.handle_input(event.pos)
        gui.render()
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__':
    main()