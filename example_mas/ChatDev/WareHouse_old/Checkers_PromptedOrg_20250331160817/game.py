'''
Defines the Game class for managing the game flow and player interactions.
'''
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'white'
    def play(self):
        while not self.check_win():
            self.board.display_board()
            print(f"{self.current_player}'s turn")
            move = self.prompt_move(self.current_player)
            from_pos, to_pos = move
            if self.board.is_valid_move(from_pos, to_pos):
                self.board.move_piece(from_pos, to_pos)
                while self.board.is_valid_capture(to_pos, (to_pos[0] + 2, to_pos[1] + 2)) or \
                      self.board.is_valid_capture(to_pos, (to_pos[0] + 2, to_pos[1] - 2)) or \
                      self.board.is_valid_capture(to_pos, (to_pos[0] - 2, to_pos[1] + 2)) or \
                      self.board.is_valid_capture(to_pos, (to_pos[0] - 2, to_pos[1] - 2)):
                    self.board.display_board()
                    print(f"Additional capture available for {self.current_player}.")
                    move = self.prompt_move(self.current_player)
                    from_pos, to_pos = move
                    if self.board.is_valid_move(from_pos, to_pos):
                        self.board.move_piece(from_pos, to_pos)
                self.switch_player()
            else:
                print("Invalid move. Try again.")
    def check_win(self):
        white_pieces = 0
        black_pieces = 0
        for row in self.board.board:
            for piece in row:
                if piece is not None:
                    if piece.color == 'white':
                        white_pieces += 1
                    elif piece.color == 'black':
                        black_pieces += 1
        if white_pieces == 0:
            print("Black wins!")
            return True
        elif black_pieces == 0:
            print("White wins!")
            return True
        return False
    def prompt_move(self, player):
        while True:
            try:
                move = input("Enter your move (e.g., '2,3 to 3,4'): ")
                from_str, to_str = move.split(' to ')
                from_pos = tuple(map(int, from_str.split(',')))
                to_pos = tuple(map(int, to_str.split(',')))
                return from_pos, to_pos
            except ValueError:
                print("Invalid input format. Please enter the move as 'x1,y1 to x2,y2'.")
    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'