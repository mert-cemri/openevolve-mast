'''
Main entry point for the 2048 game application using Pygame.
'''
import pygame
from game import Game
# Constants
GRID_SIZE = 10
TILE_SIZE = 50
TILE_MARGIN = 5
SCREEN_WIDTH = GRID_SIZE * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
SCREEN_HEIGHT = GRID_SIZE * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
FPS = 60
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('2048 Game - 10x10 Grid')
    clock = pygame.time.Clock()
    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move('left')
                elif event.key == pygame.K_RIGHT:
                    game.move('right')
                elif event.key == pygame.K_UP:
                    game.move('up')
                elif event.key == pygame.K_DOWN:
                    game.move('down')
        screen.fill((187, 173, 160))
        game.grid.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
if __name__ == '__main__':
    main()