'''
Represents the game board and manages board state.
'''
import pygame
from piece import Piece
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    def setup_pieces(self):
        # Place black pieces
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('black', (row, col))
        # Place white pieces
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('white', (row, col))
    def draw(self, screen):
        # Draw the board and pieces
        for row in range(8):
            for col in range(8):
                color = (139, 69, 19) if (row + col) % 2 == 0 else (255, 228, 196)
                pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))
                piece = self.grid[row][col]
                if piece:
                    piece_color = (0, 0, 0) if piece.color == 'black' else (255, 255, 255)
                    pygame.draw.circle(screen, piece_color, (col * 100 + 50, row * 100 + 50), 40)
                    if piece.is_king:
                        pygame.draw.circle(screen, (255, 215, 0), (col * 100 + 50, row * 100 + 50), 20)
    def update(self, move, player):
        start, end = move
        start_row, start_col = start
        end_row, end_col = end
        piece = self.grid[start_row][start_col]
        if piece and piece.color == player:
            if self.is_valid_move(start, end, player):
                self.grid[end_row][end_col] = piece
                self.grid[start_row][start_col] = None
                piece.move((end_row, end_col))
                # Check for kinging
                if (player == 'black' and end_row == 7) or (player == 'white' and end_row == 0):
                    piece.king()
                # Handle capture
                if abs(start_row - end_row) == 2:
                    capture_row = (start_row + end_row) // 2
                    capture_col = (start_col + end_col) // 2
                    self.grid[capture_row][capture_col] = None
                return True
        return False
    def is_valid_move(self, start, end, player):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.grid[start_row][start_col]
        if not piece or piece.color != player:
            return False
        direction = 1 if player == 'black' else -1
        if piece.is_king:
            direction = [1, -1]
        else:
            direction = [direction]
        # Normal move
        if (end_row, end_col) in [(start_row + d, start_col + 1) for d in direction] + [(start_row + d, start_col - 1) for d in direction]:
            return self.grid[end_row][end_col] is None
        # Capture move
        if (end_row, end_col) in [(start_row + 2 * d, start_col + 2) for d in direction] + [(start_row + 2 * d, start_col - 2) for d in direction]:
            capture_row = (start_row + end_row) // 2
            capture_col = (start_col + end_col) // 2
            capture_piece = self.grid[capture_row][capture_col]
            return capture_piece and capture_piece.color != player and self.grid[end_row][end_col] is None
        return False