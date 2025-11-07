'''
This module contains the InputHandler class which handles input from the user, either from a file or direct input.
'''
class InputHandler:
    def __init__(self, source):
        self.source = source
    def read_board(self):
        '''
        Public method to read the Sudoku board from the specified source.
        Returns the board as a list of lists.
        '''
        if isinstance(self.source, str):
            return self._read_from_file(self.source)
        elif isinstance(self.source, list):
            return self._read_from_list(self.source)
        else:
            raise ValueError("Unsupported input source")
    def _read_from_file(self, filename):
        '''
        Private method to read the Sudoku board from a file.
        Returns the board as a list of lists.
        '''
        with open(filename, 'r') as file:
            lines = file.readlines()
        return self._parse_board(lines)
    def _read_from_list(self, board_list):
        '''
        Private method to read the Sudoku board from a list.
        Returns the board as a list of lists.
        '''
        return self._parse_board(board_list)
    def _parse_board(self, lines):
        '''
        Private method to parse the Sudoku board from a list of strings.
        Returns the board as a list of lists.
        '''
        board = []
        for line in lines:
            try:
                row = [int(num) for num in line.strip().split()]
                if len(row) != 9:
                    raise ValueError("Each row must contain exactly 9 numbers.")
                board.append(row)
            except ValueError as ve:
                raise ValueError(f"Invalid input in board: {ve}")
        if len(board) != 9:
            raise ValueError("The board must contain exactly 9 rows.")
        return board