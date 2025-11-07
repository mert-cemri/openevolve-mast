'''
This is the main file for the Gomoku game. It initializes the game and starts the game loop.
'''
from board import Board
from player import Player
class Game:
    def __init__(self, size=15):
        self.board = Board(size)
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1
    def play_turn(self, x, y):
        if self.board.is_valid_move(x, y):
            self.board.place_piece(x, y, self.current_player.symbol)
            if self.check_win(x, y):
                print(f"Player {self.current_player.symbol} wins!")
                return True
            if self.check_draw():
                print("The game is a draw!")
                return True
            self.switch_player()
        else:
            print("Invalid move. Try again.")
        return False
    def check_win(self, x, y):
        # Check for five in a row in all directions
        return self.board.check_five_in_a_row(x, y, self.current_player.symbol)
    def check_draw(self):
        return self.board.is_full()
    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
def main():
    game = Game()
    game.board.display()
    while True:
        try:
            move = input(f"Player {game.current_player.symbol}, enter your move (row and column): ")
            x, y = map(int, move.split())
            if not (0 <= x < game.board.size and 0 <= y < game.board.size):
                print("Invalid input. Please ensure the row and column numbers are within the board size.")
                continue
            if game.play_turn(x, y):
                break
            game.board.display()
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
if __name__ == "__main__":
    main()