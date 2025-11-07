'''
Main entry point for the Reversi game. Initializes the game and handles the main game loop.
'''
import pygame
from game import Game
from board import Board
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption('Reversi')
    clock = pygame.time.Clock()
    game = Game()
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // 80, x // 80
                if game.make_move(row, col):
                    if game.is_game_over():
                        print("Game Over!")
                        print(f"Winner: {game.get_winner()}")
                        running = False
                    else:
                        game.switch_player()
        screen.fill((0, 0, 0))
        board.draw_board(screen)
        board.draw_discs(screen, game.board)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    main()