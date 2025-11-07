'''
Game class to manage the overall state and flow of the Reversi game.
'''
from board import Board
from player import Player
class Game:
    def __init__(self):
        '''
        Initialize the game with a board and two players.
        '''
        self.board = Board()
        self.players = [Player('B'), Player('W')]
        self.current_turn = 0  # Index of the current player
    def start(self):
        '''
        Start the game loop, alternating turns between players.
        '''
        while not self.board.is_full() and (self.board.has_valid_moves(self.players[0].color) or self.board.has_valid_moves(self.players[1].color)):
            self.board.display()
            current_player = self.players[self.current_turn]
            print(f"Player {current_player.color}'s turn.")
            move = current_player.get_move(self.board)
            if move:
                self.board.place_disc(move, current_player.color)
            else:
                print("No valid moves available. Skipping turn.")
            self.current_turn = 1 - self.current_turn  # Switch turns
        self.end_game()
    def end_game(self):
        '''
        Determine and announce the winner of the game.
        '''
        self.board.display()
        black_score, white_score = self.board.get_scores()
        if black_score > white_score:
            print("Player B wins!")
        elif white_score > black_score:
            print("Player W wins!")
        else:
            print("It's a tie!")