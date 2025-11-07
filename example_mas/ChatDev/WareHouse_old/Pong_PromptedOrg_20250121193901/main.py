'''
Main script to initialize and run the Pong game.
'''
import pygame
from game import Game
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong Game')
    game = Game(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.update()
        game.render()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == '__main__':
    main()