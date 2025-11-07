'''
Game logic class handling bidding, validation, and gameplay.
'''
class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.landlord = None
        self.current_player_index = 0
        self.last_played_cards = []
        self.last_player_index = None
    def start_game(self):
        # Bidding phase
        for i, player in enumerate(self.players):
            if player.bid():
                self.landlord = player
                player.is_landlord = True
                player.hand += self.deck.bottom_cards
                player.hand.sort(key=lambda c: c.value())
                self.current_player_index = i
                print(f"{player.name} is the landlord.")
                break
        if not self.landlord:
            self.landlord = self.players[0]
            self.landlord.is_landlord = True
            self.landlord.hand += self.deck.bottom_cards
            self.landlord.hand.sort(key=lambda c: c.value())
            print(f"No bids. {self.landlord.name} is the landlord by default.")
        # Gameplay loop
        while True:
            current_player = self.players[self.current_player_index]
            print(f"\n{current_player.name}'s turn.")
            played_cards = current_player.play_cards()
            if not played_cards:
                print(f"{current_player.name} passes.")
            elif self.validate_play(played_cards):
                if not self.last_played_cards or self.compare_combinations(self.last_played_cards, played_cards):
                    self.last_played_cards = played_cards
                    self.last_player_index = self.current_player_index
                    print(f"{current_player.name} played: {' '.join(str(c) for c in played_cards)}")
                else:
                    print("Invalid play. You must beat the previous combination.")
                    current_player.hand += played_cards  # Return cards to hand
                    current_player.hand.sort(key=lambda c: c.value())
                    continue
            else:
                print("Invalid combination. Try again.")
                current_player.hand += played_cards  # Return cards to hand
                current_player.hand.sort(key=lambda c: c.value())
                continue
            if not current_player.hand:
                print(f"\n{current_player.name} wins!")
                break
            self.current_player_index = (self.current_player_index + 1) % 3
    def validate_play(self, cards):
        # Simplified validation: only singles, pairs, and jokers
        if len(cards) == 1:
            return True
        elif len(cards) == 2 and cards[0].rank == cards[1].rank:
            return True
        elif len(cards) == 2 and {'Black Joker', 'Red Joker'} == {cards[0].rank, cards[1].rank}:
            return True
        return False
    def compare_combinations(self, prev_cards, new_cards):
        # Simplified comparison logic
        if len(prev_cards) != len(new_cards):
            if len(new_cards) == 2 and {'Black Joker', 'Red Joker'} == {new_cards[0].rank, new_cards[1].rank}:
                return True  # Joker bomb beats anything
            return False
        return new_cards[0].value() > prev_cards[0].value()