'''
Main file to run the Reversi (Othello) game using Pygame.
'''
import pygame
from game import Game
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Reversi (Othello)')
    clock = pygame.time.Clock()
    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                game.handle_click(x, y)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == '__main__':
    main()