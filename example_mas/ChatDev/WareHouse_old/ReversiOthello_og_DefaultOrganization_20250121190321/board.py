'''
Handles the visual representation of the Reversi board and discs.
'''
import pygame
class Board:
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(col * 80, row * 80, 80, 80)
                pygame.draw.rect(screen, (0, 128, 0), rect)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
    def draw_discs(self, screen, board):
        for row in range(8):
            for col in range(8):
                if board[row][col] is not None:
                    color = (255, 255, 255) if board[row][col] == 'W' else (0, 0, 0)
                    pygame.draw.circle(screen, color, (col * 80 + 40, row * 80 + 40), 30)