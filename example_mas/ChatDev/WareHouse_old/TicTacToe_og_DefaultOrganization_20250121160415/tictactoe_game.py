'''
Game logic for the Tic-Tac-Toe game.
'''
class TicTacToeGame:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.winner:
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False
    def check_winner(self):
        # Check rows, columns, and diagonals
        lines = self.board + [list(col) for col in zip(*self.board)] + [
            [self.board[i][i] for i in range(3)],
            [self.board[i][2 - i] for i in range(3)]
        ]
        for line in lines:
            if line[0] == line[1] == line[2] != "":
                self.winner = line[0]
                return self.winner
        if all(cell != "" for row in self.board for cell in row):
            self.winner = "Draw"
            return self.winner
        return None