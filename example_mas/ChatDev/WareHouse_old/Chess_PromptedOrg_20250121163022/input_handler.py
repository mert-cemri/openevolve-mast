'''
Handles user input and validates moves.
'''
class InputHandler:
    def parse_input(self, input_str):
        # Convert input like 'Ke8' to board coordinates
        piece, col, row = input_str[0], input_str[1], input_str[2]
        start_pos = (8 - int(row), ord(col) - ord('a'))
        end_pos = (8 - int(input_str[3]), ord(input_str[4]) - ord('a'))
        return start_pos, end_pos
    def validate_input(self, input_str):
        # Validate input format
        if len(input_str) == 5 and input_str[0] in 'KQRBNP' and input_str[1] in 'abcdefgh' and input_str[2] in '12345678' and input_str[3] in 'abcdefgh' and input_str[4] in '12345678':
            return True
        return False