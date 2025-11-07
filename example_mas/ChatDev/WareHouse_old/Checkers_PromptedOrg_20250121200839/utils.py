'''
Contains utility functions like parsing user input for moves.
'''
def parse_move(move):
    # Convert move notation (e.g., 'A3-B4') into board coordinates
    start, end = move.split('-')
    start_pos = (int(start[1]) - 1, ord(start[0].upper()) - ord('A'))
    end_pos = (int(end[1]) - 1, ord(end[0].upper()) - ord('A'))
    return start_pos, end_pos