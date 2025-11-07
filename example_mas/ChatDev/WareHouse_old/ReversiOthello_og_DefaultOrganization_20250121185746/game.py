'''
Game class to manage the overall game state and logic.
'''
import pygame
from board import Board
from player import Player
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player('black'), Player('white')]
        self.current_player_index = 0
        self.game_over = False
    def reset_game(self):
        self.board = Board()
        self.current_player_index = 0
        self.game_over = False
    def handle_click(self, x, y):
        if self.game_over:
            return
        grid_x, grid_y = x // 100, y // 100
        if self.board.is_valid_move(grid_x, grid_y, self.current_player()):
            self.board.update_board(grid_x, grid_y, self.current_player())
            self.switch_player()
            if not self.board.get_valid_moves(self.current_player()):
                self.switch_player()
                if not self.board.get_valid_moves(self.current_player()):
                    self.game_over = True
    def draw(self, screen):
        self.board.draw_board(screen)
    def current_player(self):
        return self.players[self.current_player_index]
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index