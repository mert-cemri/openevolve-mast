'''
CheckersGame class to manage the game logic.
'''
from board import Board
from piece import Piece
from utils import parse_move_input
class CheckersGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'B'  # 'B' for Black, 'W' for White
    def play(self):
        while not self.is_game_over():
            self.board.display()
            move = input(f"Player {self.current_player}, enter your move (e.g., 'A3-B4'): ")
            from_pos, to_pos = parse_move_input(move)
            if self.is_valid_move(from_pos, to_pos):
                self.move_piece(from_pos, to_pos)
                if self.should_king(to_pos):
                    self.king_piece(to_pos)
                self.switch_player()
            else:
                print("Invalid move. Try again.")
    def move_piece(self, from_pos, to_pos):
        piece = self.board.get_piece(from_pos)
        self.board.update_position(from_pos, None)
        self.board.update_position(to_pos, piece)
        if abs(from_pos[0] - to_pos[0]) == 2:
            self.capture_piece(from_pos, to_pos)
    def capture_piece(self, from_pos, to_pos):
        mid_x = (from_pos[0] + to_pos[0]) // 2
        mid_y = (from_pos[1] + to_pos[1]) // 2
        self.board.update_position((mid_x, mid_y), None)
    def king_piece(self, pos):
        piece = self.board.get_piece(pos)
        piece.make_king()
    def is_valid_move(self, from_pos, to_pos):
        piece = self.board.get_piece(from_pos)
        if piece is None or piece.color != self.current_player:
            return False
        if self.board.get_piece(to_pos) is not None:
            return False
        dx = to_pos[0] - from_pos[0]
        dy = to_pos[1] - from_pos[1]
        if abs(dx) != abs(dy) or abs(dx) > 2:
            return False
        if abs(dx) == 2:
            mid_x = (from_pos[0] + to_pos[0]) // 2
            mid_y = (from_pos[1] + to_pos[1]) // 2
            mid_piece = self.board.get_piece((mid_x, mid_y))
            if mid_piece is None or mid_piece.color == self.current_player:
                return False
        return True
    def is_game_over(self):
        # Check if one player has no pieces left or no valid moves
        return not any(self.board.get_piece((x, y)) is not None and self.board.get_piece((x, y)).color == self.current_player for x in range(8) for y in range(8))
    def switch_player(self):
        self.current_player = 'W' if self.current_player == 'B' else 'B'
    def should_king(self, pos):
        piece = self.board.get_piece(pos)
        if piece.color == 'B' and pos[0] == 7:  # Check x-coordinate for Black
            return True
        if piece.color == 'W' and pos[0] == 0:  # Check x-coordinate for White
            return True
        return False