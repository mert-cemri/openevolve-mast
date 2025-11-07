'''
Main file to initialize and run the Reversi game using Pygame.
'''
import pygame
from game import Game
from board import Board
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Reversi (Othello)')
    clock = pygame.time.Clock()
    game = Game()
    board = Board(game)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                board.handle_click(x, y)
        screen.fill((0, 0, 0))
        board.draw_board(screen)
        pygame.display.flip()
        if game.is_game_over():
            print("Game over. No more valid moves.")
            running = False
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    main()