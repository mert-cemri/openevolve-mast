'''
This module contains the ConnectFourGame class, which manages the game logic for Connect Four.
'''
class ConnectFourGame:
    ROWS = 6
    COLUMNS = 7
    EMPTY = ' '
    def __init__(self):
        '''Initialize the game board and set the starting player.'''
        self.board = [[self.EMPTY for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self.current_player = 'X'
    def display_board(self):
        '''Display the current state of the game board with clear cell boundaries.'''
        print("\nCurrent Board:")
        print('-' * (self.COLUMNS * 4 + 1))
        for row in self.board:
            print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
            print('-' * (self.COLUMNS * 4 + 1))
        print('  ' + '   '.join(str(i) for i in range(self.COLUMNS)))
    def is_valid_move(self, column):
        '''Check if the move is valid (column is within bounds and not full).'''
        return 0 <= column < self.COLUMNS and self.board[0][column] == self.EMPTY
    def make_move(self, column):
        '''Place the current player's disc in the chosen column.'''
        for row in reversed(range(self.ROWS)):
            if self.board[row][column] == self.EMPTY:
                self.board[row][column] = self.current_player
                return row, column
        raise ValueError("Column is full")
    def check_winner(self, row, column):
        '''Check if the current move resulted in a win.'''
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for step in [1, -1]:
                r, c = row, column
                while True:
                    r += dr * step
                    c += dc * step
                    if 0 <= r < self.ROWS and 0 <= c < self.COLUMNS and self.board[r][c] == self.current_player:
                        count += 1
                    else:
                        break
            if count >= 4:
                return True
        return False
    def is_board_full(self):
        '''Check if the board is full, indicating a draw.'''
        return all(self.board[0][col] != self.EMPTY for col in range(self.COLUMNS))
    def switch_player(self):
        '''Switch the current player.'''
        self.current_player = 'O' if self.current_player == 'X' else 'X'