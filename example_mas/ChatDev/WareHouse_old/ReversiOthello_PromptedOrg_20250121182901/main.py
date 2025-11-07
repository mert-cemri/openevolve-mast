'''
Main module to run the Reversi (Othello) game.
'''
from board import Board
from player import Player
from game import Game
def main():
    # Initialize the game
    board = Board()
    player1 = Player('B')  # Black player
    player2 = Player('W')  # White player
    game = Game(board, player1, player2)
    # Start the game loop
    while not game.is_game_over():
        board.display()
        current_player = game.current_player
        print(f"Player {current_player.color}'s turn.")
        valid_moves = board.get_valid_moves(current_player.color)
        if valid_moves:
            move = current_player.make_move(valid_moves)
            game.play_move(move)
        else:
            print(f"No valid moves for Player {current_player.color}. Skipping turn.")
            game.skip_turn()
    # Display the final board and the winner
    board.display()
    winner = game.get_winner()
    if winner:
        print(f"The winner is Player {winner.color}!")
    else:
        print("The game is a draw!")
if __name__ == "__main__":
    main()