'''
Utility functions for the Checkers game.
'''
def parse_move_input(move):
    # Parse move input and return from and to positions
    from_pos, to_pos = move.split('-')
    return parse_position(from_pos), parse_position(to_pos)
def parse_position(pos):
    # Convert board position from notation to indices
    letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    x = letter_to_index[pos[0].upper()]
    y = int(pos[1]) - 1
    return x, y