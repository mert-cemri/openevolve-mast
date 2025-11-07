'''
Main executable script that implements the game loop, handles user input, alternates turns between players, validates moves, updates the board state, and checks for a winner. Now supports multiple sequential captures.
'''
from board import Board
def parse_move(move_str):
    try:
        from_str, to_str = move_str.split('-')
        from_pos = tuple(map(int, from_str.split(',')))
        to_pos = tuple(map(int, to_str.split(',')))
        if all(0 <= n <= 7 for n in from_pos + to_pos):
            return from_pos, to_pos
        else:
            return None, None
    except:
        return None, None
def main():
    board = Board()
    current_player = 'W'
    player_names = {'W': 'White', 'B': 'Black'}
    continue_capture = False
    from_pos = None
    while True:
        board.draw_board()
        print(f"{player_names[current_player]}'s turn.")
        if continue_capture:
            print(f"You must continue capturing with the piece at position {from_pos}.")
            move_input = input(f"Enter your next capture move from {from_pos} (e.g., {from_pos[0]},{from_pos[1]}-x,y): ")
        else:
            move_input = input("Enter your move (e.g., 5,0-4,1): ")
        new_from_pos, to_pos = parse_move(move_input)
        if new_from_pos is None or to_pos is None:
            print("Invalid input format or out-of-bounds positions. Please try again.")
            continue
        if continue_capture and new_from_pos != from_pos:
            print(f"You must continue capturing with the same piece at position {from_pos}.")
            continue
        if not board.valid_move(new_from_pos, to_pos, current_player):
            print("Invalid move. Please try again.")
            continue
        board.move_piece(new_from_pos, to_pos)
        # Check for additional captures
        if abs(new_from_pos[0] - to_pos[0]) == 2 and board.has_capture_moves(to_pos):
            continue_capture = True
            from_pos = to_pos
            continue
        else:
            continue_capture = False
            from_pos = None
        winner = board.check_winner()
        if winner:
            board.draw_board()
            print(f"{winner} wins the game!")
            break
        current_player = 'B' if current_player == 'W' else 'W'
if __name__ == "__main__":
    main()