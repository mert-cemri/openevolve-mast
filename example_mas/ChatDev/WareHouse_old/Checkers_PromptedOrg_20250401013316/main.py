'''
Main file to run the Checkers game with mandatory capture rules and multiple sequential captures enforced.
'''
from board import Board
def parse_input(move_str):
    try:
        from_pos, to_pos = move_str.split('-')
        from_pos = (int(from_pos[1])-1, ord(from_pos[0].lower())-ord('a'))
        to_pos = (int(to_pos[1])-1, ord(to_pos[0].lower())-ord('a'))
        return from_pos, to_pos
    except:
        return None, None
def main():
    board = Board()
    current_player = 'W'
    while not board.has_winner():
        board.display()
        print(f"Player {current_player}'s turn (e.g., b6-a5):")
        if board.has_capture_moves(current_player):
            print("Capture move available! You must perform a capture.")
        move_str = input().strip()
        from_pos, to_pos = parse_input(move_str)
        if from_pos is None or not board.valid_move(from_pos, to_pos, current_player):
            print("Invalid move. Try again.")
            continue
        captured = board.move_piece(from_pos, to_pos)
        # Handle multiple sequential captures
        while captured and board.has_capture_moves_from_position(to_pos, current_player):
            board.display()
            print(f"Player {current_player}, you must continue capturing with the same piece at {chr(to_pos[1]+ord('a'))}{to_pos[0]+1}:")
            move_str = input().strip()
            new_from_pos, new_to_pos = parse_input(move_str)
            if new_from_pos != to_pos or not board.valid_move(new_from_pos, new_to_pos, current_player):
                print("Invalid move. You must continue capturing with the same piece. Try again.")
                continue
            captured = board.move_piece(new_from_pos, new_to_pos)
            to_pos = new_to_pos
        # Switch player
        current_player = 'B' if current_player == 'W' else 'W'
    board.display()
    print(f"Player {board.has_winner()} wins!")
if __name__ == "__main__":
    main()