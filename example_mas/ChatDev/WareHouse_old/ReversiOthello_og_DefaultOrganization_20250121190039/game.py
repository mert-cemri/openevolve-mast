'''
Game logic for Reversi, managing the game state and rules.
'''
class Game:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_player = 'black'
        self.initialize_board()
    def initialize_board(self):
        self.board[3][3] = 'white'
        self.board[3][4] = 'black'
        self.board[4][3] = 'black'
        self.board[4][4] = 'white'
    def make_move(self, x, y):
        if self.is_valid_move(x, y):
            flipped = self.flip_discs(x, y)
            if flipped:  # Only place the piece if discs are flipped
                self.board[x][y] = self.current_player
                self.switch_player()
    def is_valid_move(self, x, y):
        if self.board[x][y] is not None:
            return False
        # Check all directions for valid moves
        return any(self.check_direction(x, y, dx, dy) for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    def check_direction(self, x, y, dx, dy):
        i, j = x + dx, y + dy
        if not (0 <= i < 8 and 0 <= j < 8) or self.board[i][j] != self.opponent():
            return False
        i += dx
        j += dy
        while 0 <= i < 8 and 0 <= j < 8:
            if self.board[i][j] is None:
                return False
            if self.board[i][j] == self.current_player:
                return True
            i += dx
            j += dy
        return False
    def flip_discs(self, x, y):
        flipped = False
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if self.check_direction(x, y, dx, dy):
                self.flip_direction(x, y, dx, dy)
                flipped = True
        return flipped
    def flip_direction(self, x, y, dx, dy):
        i, j = x + dx, y + dy
        while self.board[i][j] == self.opponent():
            self.board[i][j] = self.current_player
            i += dx
            j += dy
    def opponent(self):
        return 'white' if self.current_player == 'black' else 'black'
    def switch_player(self):
        self.current_player = self.opponent()
    def is_game_over(self):
        current_player_moves = any(self.is_valid_move(x, y) for x in range(8) for y in range(8))
        self.switch_player()
        opponent_moves = any(self.is_valid_move(x, y) for x in range(8) for y in range(8))
        self.switch_player()  # Switch back to the original player
        return not (current_player_moves or opponent_moves)
    def get_valid_moves(self):
        return [(x, y) for x in range(8) for y in range(8) if self.is_valid_move(x, y)]