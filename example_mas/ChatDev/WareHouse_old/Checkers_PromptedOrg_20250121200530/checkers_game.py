'''
Manages the overall game flow and player interactions.
'''
from board import Board
class CheckersGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'black'
    def is_valid_move_format(self, move):
        if len(move) != 5 or move[2] != '-':
            return False
        start, end = move.split('-')
        if len(start) != 2 or len(end) != 2:
            return False
        if not (start[0].isalpha() and start[1].isdigit() and end[0].isalpha() and end[1].isdigit()):
            return False
        return True
    def play(self):
        while not self.is_game_over():
            self.board.display()
            print(f"{self.current_player}'s turn")
            move = input("Enter your move (e.g., A3-B4): ")
            if not self.is_valid_move_format(move):
                print("Invalid move format. Please enter a move in the format A3-B4.")
                continue
            try:
                if self.board.move_piece(move, self.current_player):
                    while self.board.can_continue_capture(move):
                        self.board.display()
                        print(f"{self.current_player} can continue capturing")
                        move = input("Enter your next capture move (e.g., B4-D6): ")
                        if not self.is_valid_move_format(move) or not self.board.move_piece(move, self.current_player):
                            print("Invalid move. Ending turn.")
                            break
                    self.switch_turn()
                else:
                    print("Invalid move. Try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")
    def switch_turn(self):
        self.current_player = 'white' if self.current_player == 'black' else 'black'
    def is_game_over(self):
        # Check if one player has no pieces left or no valid moves
        return self.board.is_player_out_of_moves('black') or self.board.is_player_out_of_moves('white')