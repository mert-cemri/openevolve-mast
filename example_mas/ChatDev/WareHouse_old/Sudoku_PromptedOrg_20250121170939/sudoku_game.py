'''
Defines the SudokuGame class to manage the game flow.
'''
class SudokuGame:
    def __init__(self, board, input_handler=None):
        self.board = board
        self.input_handler = input_handler or self.default_input_handler
    def start_game(self):
        print("Welcome to Sudoku!")
        while not self.board.is_complete():
            self.board.print_board()
            mistakes = self.check_for_mistakes()
            if mistakes:
                print("Mistakes found at positions:", mistakes)
            row, col, num = self.input_handler()
            if self.board.is_valid_move(row, col, num):
                self.board.grid[row][col] = num
            else:
                print("Invalid move. Try again.")
        if not self.check_for_mistakes():
            print("Congratulations! You have completed the Sudoku puzzle.")
        else:
            print("Puzzle completed, but there are mistakes.")
    def default_input_handler(self):
        while True:
            try:
                row = int(input("Enter row (0-8): "))
                col = int(input("Enter column (0-8): "))
                num = int(input("Enter number (1-9): "))
                if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                    return row, col, num
            except ValueError:
                pass
            print("Invalid input. Please enter numbers within the specified range.")
    def check_for_mistakes(self):
        mistakes = []
        for i in range(9):
            for j in range(9):
                num = self.board.grid[i][j]
                if num != 0:
                    self.board.grid[i][j] = 0
                    if not self.board.is_valid_move(i, j, num):
                        mistakes.append((i, j, num))
                    self.board.grid[i][j] = num
        return mistakes