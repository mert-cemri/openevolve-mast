'''
Manages the overall game flow and player interactions.
'''
from chessboard import ChessBoard
from player import Player
from piece import Pawn, Rook, Knight, Bishop, Queen, King
class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.players = [Player('White'), Player('Black')]
        self.current_turn = 0
    def play(self):
        while True:
            self.board.display_board()
            player = self.players[self.current_turn]
            move = player.make_move()
            if self.is_valid_move(move):
                self.board.move_piece(*move)
                self.current_turn = 1 - self.current_turn
            else:
                print("Invalid move. Try again.")
    def is_valid_move(self, move):
        start, end = move
        piece_char = self.board.board[start[0]][start[1]]
        if piece_char == ' ':
            return False
        if self.board.is_occupied_by_same_color(start, end):
            return False
        piece = self.get_piece(piece_char)
        return piece.is_valid_move(start, end, self.board.board)
    def get_piece(self, piece_char):
        color = 'white' if piece_char.isupper() else 'black'
        piece_map = {
            'P': Pawn,
            'R': Rook,
            'N': Knight,
            'B': Bishop,
            'Q': Queen,
            'K': King
        }
        return piece_map[piece_char.upper()](color)