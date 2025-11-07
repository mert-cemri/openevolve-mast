'''
Defines the HandValidator class, which validates the combinations of cards played (singles, pairs, straights, etc.).
'''
from collections import Counter
class HandValidator:
    @staticmethod
    def validate(cards):
        # Implement logic to validate card combinations
        if not cards:
            return False
        card_counts = Counter(card.rank for card in cards)
        num_cards = len(cards)
        # Single card play
        if num_cards == 1:
            return True
        # Pair
        if num_cards == 2 and len(card_counts) == 1:
            return True
        # Triple
        if num_cards == 3 and len(card_counts) == 1:
            return True
        # Bomb (Four of a kind)
        if num_cards == 4 and len(card_counts) == 1:
            return True
        # Rocket (Two Jokers)
        if num_cards == 2 and all(card.rank == 'Joker' for card in cards):
            return True
        # Straight (sequence of at least five cards)
        if num_cards >= 5 and HandValidator.is_straight(card_counts):
            return True
        # More rules can be added here for other combinations
        return False
    @staticmethod
    def is_straight(card_counts):
        # Check if the cards form a straight
        ranks = '345678910JQKA2'
        indices = [ranks.index(rank) for rank in card_counts.keys()]
        indices.sort()
        # Check for consecutive indices
        return all(indices[i] + 1 == indices[i + 1] for i in range(len(indices) - 1))