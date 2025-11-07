'''
This module contains the Game class which manages the game logic for the match-3 puzzle game.
'''
import random
from board import GameBoard
class Game:
    def __init__(self, rows, cols):
        self.board = GameBoard(rows, cols)
        self.score = 0
    def make_move(self, pos1, pos2):
        if self.board.swap(pos1, pos2):
            while True:
                matches = self.board.find_matches()
                if not matches:
                    break
                self.score += self.calculate_score(matches)
                self.board.clear_matches(matches)
                self.board.drop_candies()
                self.board.fill_board()
            return True
        return False
    def calculate_score(self, matches):
        return sum(len(match) for match in matches)
    def print_score(self):
        print(f"Score: {self.score}")