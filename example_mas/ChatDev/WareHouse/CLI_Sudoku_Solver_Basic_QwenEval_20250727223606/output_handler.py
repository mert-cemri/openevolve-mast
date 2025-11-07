'''
This module contains the OutputHandler class which handles the output of the solved Sudoku grid.
'''
class OutputHandler:
    def __init__(self, board):
        self.board = board
    def print_board(self):
        '''
        Public method to print the solved Sudoku board.
        '''
        for row in self.board:
            print(" ".join(str(num) for num in row))