'''
Player class to represent a player in the Connect Four game.
'''
class Player:
    def __init__(self, name, disc):
        self.name = name
        self.disc = disc
    def make_move(self, board, input_func=input):
        while True:
            try:
                column = int(input_func(f"{self.name}, choose a column (0-6): "))
                return column
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 6.")