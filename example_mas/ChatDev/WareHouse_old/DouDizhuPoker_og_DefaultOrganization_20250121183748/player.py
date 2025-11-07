'''
Defines the Player class representing a player in the game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def receive_cards(self, cards):
        self.hand.extend(cards)
    def play_cards(self, cards):
        for card in cards:
            self.hand.remove(card)
    def validate_play(self, cards):
        # Example logic for validating a single card play
        if len(cards) == 1:
            return True  # Any single card is valid
        # Example logic for validating a pair
        if len(cards) == 2 and cards[0].rank == cards[1].rank:
            return True  # Two cards of the same rank form a valid pair
        # Logic for triples
        if len(cards) == 3 and cards[0].rank == cards[1].rank == cards[2].rank:
            return True  # Three cards of the same rank form a valid triple
        # Logic for straights (five or more consecutive cards)
        if len(cards) >= 5 and self.is_consecutive(cards):
            return True
        # Logic for full houses (a triple and a pair)
        if len(cards) == 5 and self.is_full_house(cards):
            return True
        # Logic for bombs (four cards of the same rank)
        if len(cards) == 4 and cards[0].rank == cards[1].rank == cards[2].rank == cards[3].rank:
            return True
        # Add logic for additional combinations like consecutive pairs or triples with attached cards
        # ...
        return False  # If none of the valid combinations are met
    def is_consecutive(self, cards):
        sorted_cards = sorted(cards, key=lambda card: card.rank)
        return all(sorted_cards[i].rank + 1 == sorted_cards[i + 1].rank for i in range(len(sorted_cards) - 1))
    def is_full_house(self, cards):
        ranks = [card.rank for card in cards]
        unique_ranks = set(ranks)
        return len(unique_ranks) == 2 and (ranks.count(ranks[0]) == 3 or ranks.count(ranks[0]) == 2)
    def __str__(self):
        return f"Player {self.name} with hand: {self.hand}"