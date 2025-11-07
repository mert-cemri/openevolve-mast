'''
Defines the Game class to manage the game state and user interactions.
'''
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
    def play(self):
        print("Welcome to the Match-3 Puzzle Game!")
        while True:
            self.display_board()
            x1, y1, x2, y2 = self.get_user_input()
            if x1 == 'q':
                print("Exiting the game. Thank you for playing!")
                break
            if self.is_valid_move(x1, y1, x2, y2):
                self.board.swap_candies(x1, y1, x2, y2)
                self.board.update_board()
            else:
                print("Invalid move. Try again.")
    def display_board(self):
        for row in self.board.grid:
            print(' '.join(candy.type[0] for candy in row))
        print(f"Score: {self.board.score}")
    def get_user_input(self):
        user_input = input("Enter the coordinates of the first candy (x y) or 'q' to quit: ")
        if user_input.lower() == 'q':
            return 'q', 'q', 'q', 'q'
        try:
            x1, y1 = map(int, user_input.split())
            x2, y2 = map(int, input("Enter the coordinates of the second candy (x y): ").split())
            return x1, y1, x2, y2
        except ValueError:
            print("Invalid input. Please enter numbers.")
            return self.get_user_input()
    def is_valid_move(self, x1, y1, x2, y2):
        if abs(x1 - x2) + abs(y1 - y2) == 1:
            return True
        return False