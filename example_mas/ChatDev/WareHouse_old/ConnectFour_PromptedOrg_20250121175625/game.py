'''
Game class to manage the Connect Four game logic.
'''
from board import Board
from player import Player
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0
    def play(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            column = current_player.make_move(self.board)
            if self.board.place_disc(column, current_player.disc):
                if self.check_win(current_player.disc):
                    self.board.display()
                    print(f"{current_player.name} wins!")
                    break
                if self.check_draw():
                    self.board.display()
                    print("It's a draw!")
                    break
                self.current_player_index = 1 - self.current_player_index
    def check_win(self, disc):
        # Check horizontal, vertical, and diagonal lines for a win
        return self.board.check_line(disc)
    def check_draw(self):
        # Check if the board is full
        return self.board.is_full()