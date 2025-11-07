'''
Game module to manage the Reversi game logic.
'''
class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.players = [player1, player2]
        self.current_player_index = 0
    @property
    def current_player(self):
        return self.players[self.current_player_index]
    def play_move(self, move):
        # Handle a player's move
        row, col = move
        color = self.current_player.color
        self.board.place_disc(row, col, color)
        self.board.flip_discs(row, col, color)
        self.current_player_index = 1 - self.current_player_index
    def is_valid_move(self, row, col, color):
        # Check if a move is valid
        return self.board.is_valid_move(row, col, color)
    def get_winner(self):
        # Determine the winner at the end of the game
        black_count = sum(row.count('B') for row in self.board.grid)
        white_count = sum(row.count('W') for row in self.board.grid)
        if black_count > white_count:
            return self.players[0]  # Black player
        elif white_count > black_count:
            return self.players[1]  # White player
        else:
            return None  # Draw
    def is_game_over(self):
        # Check if the game is over
        if not any(' ' in row for row in self.board.grid):
            return True
        if not self.board.get_valid_moves('B') and not self.board.get_valid_moves('W'):
            return True
        return False
    def skip_turn(self):
        # Skip the current player's turn
        self.current_player_index = 1 - self.current_player_index