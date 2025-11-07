'''
This module contains the Player class, which represents a player in the Connect Four game.
'''
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    def choose_column(self, board):
        while True:
            try:
                column = self.get_user_input()
                if 0 <= column <= 6:
                    if board.grid[0][column] == " ":
                        return column
                    else:
                        print("Column is full. Choose another column.")
                else:
                    print("Invalid column. Choose a number between 0 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def get_user_input(self):
        while True:
            try:
                return int(input(f"Player {self.symbol}, choose a column (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")