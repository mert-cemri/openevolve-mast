'''
Contains the GameBoard class to manage the tic-tac-toe board state and operations.
'''
class GameBoard:
    def __init__(self):
        '''Initializes an empty 3x3 tic-tac-toe board.'''
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    def display_board(self):
        '''Displays the current state of the board.'''
        print("\nCurrent Board:")
        for i, row in enumerate(self.board):
            print(" " + " | ".join(row))
            if i < 2:
                print("---+---+---")
        print()
    def make_move(self, row, col, player):
        '''Places a player's mark on the board if the cell is empty.'''
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    def check_winner(self, player):
        '''Checks if the specified player has won the game.'''
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    def is_full(self):
        '''Checks if the board is full (no empty spaces).'''
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))