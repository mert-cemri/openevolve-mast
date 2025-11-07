'''
Represents a player in the game.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def make_move(self, board):
        '''
        Prompts the player for a move in notation and updates the board.
        '''
        while True:
            try:
                move = input(f"{self.color} player's turn. Enter your move (e.g., '2,3 to 3,4'): ")
                from_pos, to_pos = self.parse_move(move)
                if board.is_valid_move(from_pos, to_pos):
                    if abs(from_pos[0] - to_pos[0]) == 2:
                        board.capture_piece(from_pos, to_pos)
                    else:
                        board.move_piece(from_pos, to_pos)
                    break
                else:
                    print("Invalid move. Please try again.")
            except Exception as e:
                print(f"Error: {e}. Please enter a valid move.")
    def parse_move(self, move):
        '''
        Parses the move input from the player and returns from and to positions.
        '''
        try:
            from_str, to_str = move.split(' to ')
            from_pos = tuple(map(int, from_str.split(',')))
            to_pos = tuple(map(int, to_str.split(',')))
            return from_pos, to_pos
        except ValueError:
            raise ValueError("Invalid move format. Use 'row,col to row,col'.")