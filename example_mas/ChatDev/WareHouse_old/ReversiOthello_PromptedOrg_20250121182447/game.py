'''
Manages the game flow for Reversi (Othello), including turn management and game end conditions.
'''
class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.current_player_index = 0
    def start(self):
        # Start the game loop
        while not self.board.is_full():
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.color}'s turn")
            # Check if the current player has any valid moves
            if any(self.board.is_valid_move(row, col, current_player.color) for row in range(self.board.size) for col in range(self.board.size)):
                row, col = current_player.get_move(self.board)
                if self.board.place_disc(row, col, current_player.color):
                    self.current_player_index = 1 - self.current_player_index
                else:
                    print("Invalid move. Try again.")
            else:
                print(f"No valid moves for {current_player.color}. Passing turn.")
                self.current_player_index = 1 - self.current_player_index
            # Check if both players have no valid moves
            if not any(self.board.is_valid_move(row, col, self.players[self.current_player_index].color) for row in range(self.board.size) for col in range(self.board.size)):
                break
        self.end_game()
    def end_game(self):
        # Determine the winner and print the result
        black_count = sum(row.count('B') for row in self.board.grid)
        white_count = sum(row.count('W') for row in self.board.grid)
        print("Game Over")
        print(f"Black: {black_count}, White: {white_count}")
        if black_count > white_count:
            print("Black wins!")
        elif white_count > black_count:
            print("White wins!")
        else:
            print("It's a tie!")