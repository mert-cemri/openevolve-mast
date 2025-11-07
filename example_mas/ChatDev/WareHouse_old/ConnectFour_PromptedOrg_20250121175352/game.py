'''
Game class to manage the overall game flow, including initializing the board, handling player turns, and checking for win conditions.
'''
from board import Board
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.name}'s turn. Choose a column (0-6):")
            column = None
            while column is None:
                try:
                    user_input = input().strip()
                    if user_input == "":
                        raise ValueError("Empty input")
                    column = int(user_input)
                    if column < 0 or column > 6:
                        print("Invalid column. Please choose a column between 0 and 6.")
                        column = None
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6.")
            if self.board.place_disc(column, current_player.disc):
                if self.board.check_winner(current_player.disc):
                    self.board.display()
                    print(f"{current_player.name} wins!")
                    break
                elif self.board.is_draw():
                    self.board.display()
                    print("It's a draw!")
                    break
                else:
                    self.switch_player()
            else:
                print("Column full or invalid. Try again.")