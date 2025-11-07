'''
Player class to represent a player in the Reversi game.
'''
class Player:
    def __init__(self, color):
        '''
        Initialize a player with a specific disc color.
        '''
        self.color = color
    def get_move(self, board, input_method=None):
        '''
        Get a valid move from the player using the specified input method.
        If no valid moves are available, return None.
        '''
        if not board.has_valid_moves(self.color):
            print(f"No valid moves available for {self.color}.")
            return None
        if input_method is None:
            input_method = self.default_input_method
        while True:
            try:
                move = input_method(f"Enter your move (row col) for {self.color}: ")
                x, y = map(int, move.split())
                if board.is_valid_move((x, y), self.color):
                    return (x, y)
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter row and column numbers.")
    def default_input_method(self, prompt):
        '''
        Default method for getting input from the player.
        '''
        return input(prompt)