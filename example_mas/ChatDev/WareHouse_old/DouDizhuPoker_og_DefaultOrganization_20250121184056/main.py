'''
Main entry point for the Dou Dizhu game application.
'''
import pygame
from game import Game
from gui import GameGUI
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dou Dizhu")
    game = Game()
    gui = GameGUI(screen, game)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            gui.handle_event(event)
        game.update()
        gui.render()
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()