'''
Main file to initialize and run the 2048 game with a 10x10 grid using Pygame.
'''
import pygame
from game2048 import Game2048
from renderer import Renderer
from input_handler import InputHandler
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('2048 Game - 10x10 Grid')
    game = Game2048()
    renderer = Renderer(screen, game)
    input_handler = InputHandler(game)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            input_handler.handle_input(event)
        game.check_game_over()
        renderer.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()