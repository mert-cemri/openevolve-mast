'''
Main file to run the Gomoku game.
'''
from board import Board
from player import Player
class Game:
    def __init__(self):
        '''
        Initialize the game with a board and two players.
        '''
        self.board = Board()
        self.players = [Player('B'), Player('W')]
        self.current_player_index = 0
        self.winner = None
    def play_move(self, x, y):
        '''
        Handle a player's move. Check if the move is valid, place the stone,
        and determine if the move results in a win.
        '''
        # Check if the game is already won
        if self.winner:
            print("Game over! Player", self.winner, "has already won.")
            return
        # Validate the move
        if not self.is_valid_move(x, y):
            print("Invalid move. Try again.")
            return
        current_player = self.players[self.current_player_index]
        # Place the stone and check for a winner
        if self.board.place_stone(x, y, current_player.stone):
            if self.check_winner(x, y, current_player.stone):
                self.winner = current_player.stone
                print("Player", self.winner, "wins!")
            else:
                # Switch to the other player
                self.current_player_index = 1 - self.current_player_index
    def check_winner(self, x, y, stone):
        '''
        Check if the current move results in a win by forming an unbroken row
        of five stones in any direction.
        '''
        return (self.check_line(x, y, stone, 1, 0) or  # Horizontal
                self.check_line(x, y, stone, 0, 1) or  # Vertical
                self.check_line(x, y, stone, 1, 1) or  # Diagonal /
                self.check_line(x, y, stone, 1, -1))   # Diagonal \
    def check_line(self, x, y, stone, dx, dy):
        '''
        Check for consecutive stones in both directions from the current position.
        Return true if there are 5 or more consecutive stones.
        '''
        count = 1
        # Check in both directions for consecutive stones
        for direction in [1, -1]:
            nx, ny = x + direction * dx, y + direction * dy
            while self.board.get_stone(nx, ny) == stone:
                count += 1
                nx += direction * dx
                ny += direction * dy
        # Return true if there are 5 or more consecutive stones
        return count >= 5
    def is_valid_move(self, x, y):
        '''
        Check if the move is within the board boundaries and the cell is empty.
        '''
        return 0 <= x < 15 and 0 <= y < 15 and self.board.get_stone(x, y) == '.'
    def print_board(self):
        '''
        Print the current state of the board.
        '''
        self.board.print_board()
if __name__ == "__main__":
    game = Game()
    game.print_board()
    while not game.winner:
        try:
            x, y = map(int, input(f"Player {game.players[game.current_player_index].stone}, enter your move (row and column): ").split())
            game.play_move(x, y)
            game.print_board()
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")