'''
Player module to represent a player in the Gomoku game.
'''
from utils import get_input
class Player:
    def __init__(self, name, stone):
        self.name = name
        self.stone = stone
    def make_move(self, board, input_func=input):
        return get_input(board.size, input_func)