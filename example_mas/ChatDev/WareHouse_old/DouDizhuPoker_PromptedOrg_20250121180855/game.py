'''
Module to manage the game flow of Dou Dizhu.
'''
from hand_evaluator import HandEvaluator
class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.landlord = None
        self.landlord_cards = []
    def start(self):
        # Deal cards to players
        hands, self.landlord_cards = self.deck.deal(len(self.players))
        for i, player in enumerate(self.players):
            player.receive_cards(hands[i])
        # Determine landlord
        self.determine_landlord()
        # Main game loop
        self.play_game()
    def determine_landlord(self):
        # Simple logic to choose the first player as landlord
        self.landlord = self.players[0]
        self.landlord.receive_cards(self.landlord_cards)
        print(f"{self.landlord.name} is the landlord.")
    def play_game(self):
        # Implement game loop logic
        current_player_index = 0
        while True:
            current_player = self.players[current_player_index]
            print(f"{current_player.name}'s turn with hand: {current_player.hand}")
            # Placeholder for player action
            # Here you would implement logic for the player to choose and play a valid hand
            # For now, we'll simulate a player playing a single card
            if current_player.hand:
                played_card = current_player.play_cards([current_player.hand[0]])
                if HandEvaluator.is_valid_hand(played_card):
                    print(f"{current_player.name} played: {played_card}")
                    if not current_player.hand:
                        print(f"{current_player.name} wins!")
                        break
                else:
                    print(f"Invalid hand played by {current_player.name}.")
            current_player_index = (current_player_index + 1) % len(self.players)