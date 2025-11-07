'''
Game class to manage the overall game flow.
'''
from board import Board
from player import Player
import random
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player_index = 0
        self.game_over = False
    def play(self):
        print("Welcome to Simplified Monopoly Go!")
        while not self.game_over:
            player = self.players[self.current_player_index]
            print(f"\n{player.name}'s turn. Current balance: ${player.money}")
            if player.in_jail:
                self.handle_jail(player)
            else:
                self.take_turn(player)
            self.check_game_over()
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
    def take_turn(self, player):
        input("Press Enter to roll dice...")
        dice = random.randint(1, 6)
        print(f"{player.name} rolled a {dice}")
        player.move(dice)
        self.board.handle_position(player, self.players)
        self.check_game_over()
    def handle_jail(self, player):
        print(f"{player.name} is in jail.")
        dice = random.randint(1, 6)
        print(f"{player.name} rolled a {dice}")
        if dice >= 4:
            player.in_jail = False
            print(f"{player.name} is free from jail!")
            player.move(dice)
            self.board.handle_position(player, self.players)
        else:
            print(f"{player.name} remains in jail this turn.")
    def check_game_over(self):
        for player in self.players:
            if player.money <= 0:
                self.game_over = True
                winner = [p for p in self.players if p.money > 0]
                if winner:
                    print(f"\nGame Over! {winner[0].name} wins!")
                else:
                    print("\nGame Over! All players are bankrupt!")
                break