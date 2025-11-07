'''
Contains the TicTacToeGame class to manage the game logic and player turns.
'''
from board import GameBoard
class TicTacToeGame:
    def __init__(self):
        '''Initializes the TicTacToeGame with a new board and sets the starting player to X.'''
        self.board = GameBoard()
        self.current_player = 'X'
    def switch_player(self):
        '''Switches the current player from X to O or O to X.'''
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def play(self):
        '''Main loop to play the game until there's a winner or a draw.'''
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.board.display_board()
            print(f"Player {self.current_player}'s turn.")
            row, col = self.get_player_move()
            if not self.board.make_move(row, col, self.current_player):
                print("Invalid move, the cell is already occupied. Try again.")
                continue
            if self.board.check_winner(self.current_player):
                self.board.display_board()
                print(f"Congratulations! Player {self.current_player} wins!")
                break
            if self.board.is_full():
                self.board.display_board()
                print("It's a draw!")
                break
            self.switch_player()
    def get_player_move(self):
        '''Gets valid row and column input from the player.'''
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if row in range(3) and col in range(3):
                    return row, col
                else:
                    print("Row and column must be between 1 and 3.")
            except ValueError:
                print("Please enter valid integers for row and column.")