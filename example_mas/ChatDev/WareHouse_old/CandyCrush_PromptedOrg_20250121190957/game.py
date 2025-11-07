'''
This module defines the Game class, which manages the game state and user interactions.
'''
class Game:
    def __init__(self, board):
        self.board = board
    def make_move(self, x1, y1, x2, y2):
        self.board.swap_candies(x1, y1, x2, y2)
        if self.board.find_matches():
            self.board.update_board()
        else:
            # Swap back if no matches are found
            self.board.swap_candies(x1, y1, x2, y2)
            print("No match found. Move reverted.")
    def is_valid_move(self, x1, y1, x2, y2):
        # Check if the move is within bounds and adjacent
        if abs(x1 - x2) + abs(y1 - y2) != 1:
            return False
        if not (0 <= x1 < self.board.rows and 0 <= y1 < self.board.cols):
            return False
        if not (0 <= x2 < self.board.rows and 0 <= y2 < self.board.cols):
            return False
        return True