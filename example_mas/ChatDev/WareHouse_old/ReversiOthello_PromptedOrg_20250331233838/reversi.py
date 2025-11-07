'''
Reversi (Othello) game logic implementation with robust player switching logic, clear user feedback for invalid moves, and explicit handling of game termination scenarios.
'''
class ReversiGame:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        # Initial positions
        self.board[3][3], self.board[4][4] = 'O', 'O'
        self.board[3][4], self.board[4][3] = 'X', 'X'
        self.current_player = 'X'
    def display_board(self):
        print('  ' + ' '.join(str(i) for i in range(8)))
        for i, row in enumerate(self.board):
            print(f"{i} " + ' '.join(row))
        print(f"Score - X: {self.score()['X']} | O: {self.score()['O']}")
    def valid_moves(self, player):
        opponent = 'O' if player == 'X' else 'X'
        moves = []
        for x in range(8):
            for y in range(8):
                if self.board[x][y] != ' ':
                    continue
                if self.check_move(x, y, player, opponent):
                    moves.append((x, y))
        return moves
    def check_move(self, x, y, player, opponent):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            has_opponent_between = False
            while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == opponent:
                nx += dx
                ny += dy
                has_opponent_between = True
            if has_opponent_between and 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == player:
                return True
        return False
    def make_move(self, x, y):
        opponent = 'O' if self.current_player == 'X' else 'X'
        if not (0 <= x < 8 and 0 <= y < 8):
            print("Invalid position. Please enter coordinates within the board range (0-7).")
            return False
        if self.board[x][y] != ' ':
            print("This cell is already occupied. Please choose another move.")
            return False
        if (x, y) in self.valid_moves(self.current_player):
            self.board[x][y] = self.current_player
            self.flip_discs(x, y, self.current_player, opponent)
            self.switch_player()
            return True
        else:
            print("Invalid move. No discs would be flipped. Please choose another move.")
            return False
    def flip_discs(self, x, y, player, opponent):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dx, dy in directions:
            discs_to_flip = []
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == opponent:
                discs_to_flip.append((nx, ny))
                nx += dx
                ny += dy
            if discs_to_flip and 0 <= nx < 8 and 0 <= ny < 8 and self.board[nx][ny] == player:
                for fx, fy in discs_to_flip:
                    self.board[fx][fy] = player
    def score(self):
        scores = {'X': 0, 'O': 0}
        for row in self.board:
            for cell in row:
                if cell in scores:
                    scores[cell] += 1
        return scores
    def game_over(self):
        no_moves_X = len(self.valid_moves('X')) == 0
        no_moves_O = len(self.valid_moves('O')) == 0
        board_full = all(cell != ' ' for row in self.board for cell in row)
        if board_full:
            print("The board is full. Game over.")
            return True
        elif no_moves_X and no_moves_O:
            print("No valid moves available for either player. Game over.")
            return True
        return False
    def switch_player(self):
        next_player = 'O' if self.current_player == 'X' else 'X'
        if self.valid_moves(next_player):
            self.current_player = next_player
        elif self.valid_moves(self.current_player):
            print(f"No valid moves for player {next_player}. Player {self.current_player} continues.")
        else:
            print("No valid moves available for either player. Game over.")