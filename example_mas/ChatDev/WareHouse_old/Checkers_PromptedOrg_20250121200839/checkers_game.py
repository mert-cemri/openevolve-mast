'''
Manages the overall game state, including the board, players, and turn management.
'''
from board import Board
from utils import parse_move
class CheckersGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'W'  # 'W' for White, 'B' for Black
    def play_turn(self):
        self.board.display()
        capturing_moves = self.board.get_capturing_moves(self.current_player)
        if capturing_moves:
            print(f"Player {self.current_player}, you must make a capturing move.")
            # Display possible capturing moves
            for start_pos, end_pos in capturing_moves:
                print(f"Possible capture: {start_pos} to {end_pos}")
        move = input(f"Player {self.current_player}, enter your move (e.g., 'A3-B4'): ")
        start_pos, end_pos = parse_move(move)
        if capturing_moves and (start_pos, end_pos) not in capturing_moves:
            print("Invalid move. You must capture. Try again.")
            return
        if self.board.is_valid_move(start_pos, end_pos, self.current_player):
            self.board.move_piece(start_pos, end_pos)
        else:
            print("Invalid move. Try again.")
    def check_winner(self):
        white_pieces = black_pieces = 0
        white_moves = black_moves = 0
        for row in range(8):
            for col in range(8):
                piece = self.board.grid[row][col]
                if piece is not None:
                    if piece.color == 'W':
                        white_pieces += 1
                        if self.board.is_valid_move((row, col), (row-1, col-1), 'W') or \
                           self.board.is_valid_move((row, col), (row-1, col+1), 'W'):
                            white_moves += 1
                    elif piece.color == 'B':
                        black_pieces += 1
                        if self.board.is_valid_move((row, col), (row+1, col-1), 'B') or \
                           self.board.is_valid_move((row, col), (row+1, col+1), 'B'):
                            black_moves += 1
        if white_pieces == 0 or white_moves == 0:
            print("Black wins!")
            return True
        elif black_pieces == 0 or black_moves == 0:
            print("White wins!")
            return True
        return False
    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'W' else 'W'