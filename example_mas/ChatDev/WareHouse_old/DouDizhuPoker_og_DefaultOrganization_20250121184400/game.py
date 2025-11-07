'''
Contains the Game class which manages the overall game state and logic.
'''
from deck import Deck
from player import Player
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2"), Player("Landlord")]
        self.current_turn = 0
        self.last_played_cards = None
    def start_game(self):
        self.deck.shuffle()
        self.deck.deal(self.players)
        # Additional setup logic
    def play_turn(self, cards_to_play):
        '''
        Logic for playing a turn.
        '''
        current_player = self.players[self.current_turn]
        if current_player.can_play(cards_to_play, self.last_played_cards):
            current_player.play_cards(cards_to_play)
            self.last_played_cards = cards_to_play
            print(f"{current_player.name} plays {cards_to_play}")
        else:
            print(f"Invalid move by {current_player.name}")
            return False
        self.current_turn = (self.current_turn + 1) % len(self.players)
        return True
    def check_winner(self):
        '''
        Logic to check for a winner.
        '''
        for player in self.players:
            if not player.hand:
                print(f"{player.name} wins!")
                return player
        return None