'''
Handles the graphical representation of the Reversi board using Pygame.
'''
import pygame
class Board:
    def __init__(self, game):
        self.game = game
        self.cell_size = 100
    def draw_board(self, screen):
        for x in range(8):
            for y in range(8):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (0, 128, 0), rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
                if self.game.board[x][y] is not None:
                    color = (0, 0, 0) if self.game.board[x][y] == 'black' else (255, 255, 255)
                    pygame.draw.circle(screen, color, rect.center, self.cell_size // 2 - 5)
    def handle_click(self, x, y):
        if not self.game.is_game_over():
            grid_x, grid_y = x // self.cell_size, y // self.cell_size
            self.game.make_move(grid_x, grid_y)
        else:
            print("Game over. No more valid moves.")