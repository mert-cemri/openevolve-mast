'''
Module to parse and validate chess moves.
'''
class Move:
    @staticmethod
    def parse_move(move_str):
        # Parse the move string into a structured format
        start_col = ord(move_str[0]) - ord('a')
        start_row = 8 - int(move_str[1])
        end_col = ord(move_str[2]) - ord('a')
        end_row = 8 - int(move_str[3])
        return (start_row, start_col), (end_row, end_col)
    @staticmethod
    def validate_move(move, board, color):
        # Validate the move against the board and rules
        start_pos, end_pos = move
        piece = board[start_pos[0]][start_pos[1]]
        if piece == " ":
            return False
        # Additional validation logic for each piece type
        # Implement detailed validation for each piece type
        return True