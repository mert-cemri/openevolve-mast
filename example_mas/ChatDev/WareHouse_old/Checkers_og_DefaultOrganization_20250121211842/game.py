'''
Game class to manage the overall game state and loop.
'''
import pygame
from board import Board
from player import Player
from utils import parse_move, is_valid_move
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()
        self.players = [Player('red'), Player('black')]
        self.current_turn = 0
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            move_notation = input("Enter your move (e.g., a3-b4): ")
            from_pos, to_pos = parse_move(move_notation)
            if is_valid_move(self.board, from_pos, to_pos, self.players[self.current_turn].color):
                self.board.move_piece(from_pos, to_pos)
                self.switch_turn()
            else:
                print("Invalid move. Try again.")
            self.board.draw(self.screen)
            pygame.display.flip()
    def switch_turn(self):
        self.current_turn = 1 - self.current_turn