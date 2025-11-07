'''
Manages game logic, checks, checkmate, castling, en passant, and pawn promotion.
'''
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'
    def start(self):
        while True:
            self.board.print_board()
            print(f"{self.turn.capitalize()}'s move (e.g., e2 e4):")
            move = input().split()
            start = (8-int(move[0][1]), ord(move[0][0])-ord('a'))
            end = (8-int(move[1][1]), ord(move[1][0])-ord('a'))
            piece = self.board.board[start[0]][start[1]]
            if piece and piece.color == self.turn and end in piece.valid_moves(self.board, start):
                self.board.move_piece(start, end)
                self.turn = 'black' if self.turn == 'white' else 'white'
            else:
                print("Invalid move, try again.")