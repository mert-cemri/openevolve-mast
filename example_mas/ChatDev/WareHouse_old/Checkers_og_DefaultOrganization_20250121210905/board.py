'''
Represents the game board and manages piece positions.
'''
import pygame
from piece import Piece
class Board:
    def __init__(self):
        self.board = self.initialize_board()
    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        # Initialize pieces on the board
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = Piece('Red')
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = Piece('Black')
        return board
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = (209, 139, 71) if (row + col) % 2 == 0 else (255, 206, 158)
                pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))
                piece = self.board[row][col]
                if piece:
                    piece.draw(screen, col * 100, row * 100)
    def move_piece(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        piece = self.board[from_row][from_col]
        if piece and self.is_valid_move(from_pos, to_pos):
            self.board[to_row][to_col] = piece
            self.board[from_row][from_col] = None
            if (piece.color == 'Red' and to_row == 7) or (piece.color == 'Black' and to_row == 0):
                piece.make_king()
    def capture_piece(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        mid_row = (from_row + to_row) // 2
        mid_col = (from_col + to_col) // 2
        self.board[mid_row][mid_col] = None
        self.move_piece(from_pos, to_pos)
    def is_valid_move(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        piece = self.board[from_row][from_col]
        if not piece:
            return False
        direction = 1 if piece.color == 'Red' else -1
        if piece.is_king():
            direction = [1, -1]
        if isinstance(direction, list):
            for dir in direction:
                if (to_row == from_row + dir and abs(to_col - from_col) == 1 and not self.board[to_row][to_col]):
                    return True
                if (to_row == from_row + 2 * dir and abs(to_col - from_col) == 2):
                    mid_row = (from_row + to_row) // 2
                    mid_col = (from_col + to_col) // 2
                    mid_piece = self.board[mid_row][mid_col]
                    if mid_piece and mid_piece.color != piece.color and not self.board[to_row][to_col]:
                        return True
        else:
            if (to_row == from_row + direction and abs(to_col - from_col) == 1 and not self.board[to_row][to_col]):
                return True
            if (to_row == from_row + 2 * direction and abs(to_col - from_col) == 2):
                mid_row = (from_row + to_row) // 2
                mid_col = (from_col + to_col) // 2
                mid_piece = self.board[mid_row][mid_col]
                if mid_piece and mid_piece.color != piece.color and not self.board[to_row][to_col]:
                    return True
        return False