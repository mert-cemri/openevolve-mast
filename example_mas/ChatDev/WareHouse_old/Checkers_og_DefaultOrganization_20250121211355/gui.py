'''
Handles graphical rendering and user interaction.
'''
import pygame
from utils import parse_move
class GUI:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.selected_position = None
    def render(self):
        self.screen.fill((255, 255, 255))
        self.game.board.draw(self.screen)
    def handle_input(self, mouse_pos):
        x, y = mouse_pos
        if 0 <= x < 800 and 0 <= y < 800:  # Ensure click is within board boundaries
            col, row = x // 100, y // 100
            if self.selected_position is None:
                piece = self.game.board.grid[row][col]
                if piece and piece.color == self.game.current_turn:
                    self.selected_position = (row, col)
            else:
                move = (self.selected_position, (row, col))
                if self.game.board.is_valid_move(*move, self.game.current_turn):
                    self.game.play_turn(move)
                self.selected_position = None