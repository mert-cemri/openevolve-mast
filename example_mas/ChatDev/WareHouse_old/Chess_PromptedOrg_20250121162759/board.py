'''
Module to represent and manage the chessboard.
'''
from piece import Piece
from move import Move
class Board:
    def __init__(self):
        self.board = []
    def initialize_board(self):
        # Initialize the board with pieces in starting positions
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()
    def move_piece(self, move, color):
        parsed_move = Move.parse_move(move)
        if self.is_valid_move(parsed_move, color):
            # Execute the move
            self.execute_move(parsed_move)
            return True
        return False
    def is_valid_move(self, move, color):
        # Validate the move according to chess rules
        return Move.validate_move(move, self.board, color)
    def execute_move(self, move):
        # Execute the move on the board
        start_pos, end_pos = move
        piece = self.board[start_pos[0]][start_pos[1]]
        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = " "
    def is_checkmate(self, color):
        # Check for checkmate condition
        # Implement logic to determine if the current player's king is in checkmate
        return False
    def is_stalemate(self, color):
        # Check for stalemate condition
        # Implement logic to determine if the game is in stalemate
        return False