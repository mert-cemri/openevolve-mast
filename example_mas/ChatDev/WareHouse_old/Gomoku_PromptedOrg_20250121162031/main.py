'''
Main module to run the Gomoku game.
'''
from game import Game
from player import Player
from input_handler import InputHandler
def main():
    print("Welcome to Gomoku!")
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    game = Game(player1, player2)
    input_handler = InputHandler()
    while True:
        game.board.print_board()
        current_player = game.current_player
        print(f"{current_player.name}'s turn ({current_player.stone}):")
        row = input_handler.get_valid_input("Enter row: ", game.board.size)
        col = input_handler.get_valid_input("Enter column: ", game.board.size)
        if game.play_move(row, col):
            if game.check_winner():
                game.board.print_board()
                print(f"Congratulations {current_player.name}, you win!")
                break
            elif game.is_draw():
                game.board.print_board()
                print("It's a draw!")
                break
            game.switch_player()
        else:
            print("Invalid move. Try again.")
if __name__ == "__main__":
    main()