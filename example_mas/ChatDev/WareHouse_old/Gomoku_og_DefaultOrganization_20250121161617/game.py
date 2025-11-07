'''
Game class to manage the game logic for Gomoku.
'''
import pygame
from board import Board
from player import Player
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0
        self.winner = None
    def reset_game(self):
        self.board.reset()
        self.current_player_index = 0
        self.winner = None
    def check_winner(self):
        self.winner = self.board.check_winner()
        return self.winner
    def make_move(self, x, y):
        if self.board.update_board(x, y, self.players[self.current_player_index].symbol):
            if not self.check_winner():
                self.current_player_index = (self.current_player_index + 1) % 2
    def handle_click(self, x, y):
        if not self.winner:
            grid_x = x // 40
            grid_y = y // 40
            self.make_move(grid_x, grid_y)
    def draw(self, screen):
        self.board.draw_board(screen)
        if self.winner:
            font = pygame.font.Font(None, 74)
            if self.winner == "Draw":
                text = font.render("It's a draw!", True, (0, 0, 0))
            else:
                text = font.render(f"{self.winner} wins!", True, (0, 0, 0))
            screen.blit(text, (150, 250))