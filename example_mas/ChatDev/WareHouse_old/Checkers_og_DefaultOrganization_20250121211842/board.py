'''
Board class to represent the 8x8 checkers board.
'''
import pygame
from piece import Piece
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    def setup_pieces(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('black')
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('red')
    def draw(self, screen):
        screen.fill((255, 255, 255))
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (col * 100, row * 100, 100, 100))
                if self.grid[row][col] is not None:
                    self.grid[row][col].draw(screen, (col * 100 + 50, row * 100 + 50))
    def move_piece(self, from_pos, to_pos):
        piece = self.grid[from_pos[0]][from_pos[1]]
        self.grid[to_pos[0]][to_pos[1]] = piece
        self.grid[from_pos[0]][from_pos[1]] = None
        if abs(from_pos[0] - to_pos[0]) == 2:
            self.capture_piece(((from_pos[0] + to_pos[0]) // 2, (from_pos[1] + to_pos[1]) // 2))
        if to_pos[0] == 0 or to_pos[0] == 7:
            self.king_piece(to_pos)
    def capture_piece(self, pos):
        self.grid[pos[0]][pos[1]] = None
    def king_piece(self, pos):
        piece = self.grid[pos[0]][pos[1]]
        if piece and not piece.is_king:
            piece.is_king = True