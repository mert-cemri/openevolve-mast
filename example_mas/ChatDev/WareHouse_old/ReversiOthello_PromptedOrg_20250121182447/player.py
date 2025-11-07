'''
Represents a player in the Reversi (Othello) game, handling player moves.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def get_move(self, board, input_func=input):
        # Get a valid move from the player
        while True:
            try:
                move = input_func("Enter your move (row col): ")
                row, col = map(int, move.split())
                if 0 <= row < board.size and 0 <= col < board.size:
                    if board.is_valid_move(row, col, self.color):
                        return row, col
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Move out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Enter row and column numbers.")