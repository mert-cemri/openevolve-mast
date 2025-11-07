'''
Main executable file for running the Reversi game with improved user interaction and error handling.
'''
from reversi import ReversiGame
def main():
    game = ReversiGame()
    while not game.game_over():
        game.display_board()
        moves = game.valid_moves(game.current_player)
        if not moves:
            print(f"No valid moves for player {game.current_player}.")
            game.switch_player()
            continue
        print(f"Player {game.current_player}'s turn. Valid moves: {moves}")
        try:
            x, y = map(int, input("Enter your move (row col): ").split())
            if not game.make_move(x, y):
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers separated by a space.")
    game.display_board()
    final_score = game.score()
    print("Game Over!")
    print(f"Final Score - X: {final_score['X']} | O: {final_score['O']}")
    if final_score['X'] > final_score['O']:
        print("Player X wins!")
    elif final_score['O'] > final_score['X']:
        print("Player O wins!")
    else:
        print("It's a tie!")
if __name__ == "__main__":
    main()