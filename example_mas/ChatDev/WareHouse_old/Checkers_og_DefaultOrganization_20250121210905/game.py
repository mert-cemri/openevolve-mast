'''
Manages the overall game state and game loop.
'''
import pygame
from board import Board
from player import Player
from utils import coords_to_position
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.players = [Player('Red'), Player('Black')]
        self.current_player_index = 0
        self.selected_piece = None
    def run(self):
        running = True
        while running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = coords_to_position(*pos)
                self.handle_click(row, col)
    def handle_click(self, row, col):
        if self.selected_piece:
            if self.board.is_valid_move(self.selected_piece, (row, col)):
                if abs(self.selected_piece[0] - row) == 2:
                    self.board.capture_piece(self.selected_piece, (row, col))
                else:
                    self.board.move_piece(self.selected_piece, (row, col))
                self.current_player_index = (self.current_player_index + 1) % 2
            self.selected_piece = None
        else:
            if self.board.board[row][col] and self.board.board[row][col].color == self.players[self.current_player_index].color:
                self.selected_piece = (row, col)
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.board.draw_board(self.screen)
        pygame.display.flip()