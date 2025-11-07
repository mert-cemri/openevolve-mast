'''
Module containing the TicTacToe class for game logic.
'''
class TicTacToe:
    def __init__(self):
        '''Initializes the game board and sets the starting player to X.'''
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    def display_board(self):
        '''Displays the current state of the board in a user-friendly format.'''
        print("\nCurrent board:")
        for row in range(3):
            print(" " + " | ".join(self.board[row]))
            if row < 2:
                print("---+---+---")
        print()
    def make_move(self, row, col):
        '''Places the current player's mark on the board if the position is empty.'''
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    def check_winner(self):
        '''
        Checks if the current player has won the game immediately after their move.
        Returns True if the current player has three marks in a row, column, or diagonal.
        '''
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False
    def is_board_full(self):
        '''Checks if the board is full.'''
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))
    def switch_player(self):
        '''Switches the current player from X to O or vice versa.'''
        self.current_player = 'O' if self.current_player == 'X' else 'X'