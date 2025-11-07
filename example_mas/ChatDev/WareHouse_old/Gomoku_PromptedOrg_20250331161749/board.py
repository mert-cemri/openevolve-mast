'''
Board class to represent the 15x15 Gomoku board.
'''
class Board:
    def __init__(self):
        '''
        Initialize the board with a 15x15 grid filled with '.' to represent empty spaces.
        '''
        self.size = 15
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
    def place_stone(self, x, y, stone):
        '''
        Place a stone on the board at the specified coordinates if the cell is empty.
        Return True if the stone is placed successfully, otherwise False.
        '''
        if self.get_stone(x, y) == '.':
            self.grid[x][y] = stone
            return True
        return False
    def get_stone(self, x, y):
        '''
        Return the stone at the specified coordinates, or None if out of bounds.
        '''
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.grid[x][y]
        return None
    def print_board(self):
        '''
        Print the board to the console.
        '''
        for row in self.grid:
            print(' '.join(row))