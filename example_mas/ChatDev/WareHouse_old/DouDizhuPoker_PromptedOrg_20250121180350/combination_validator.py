'''
Validates card combinations.
'''
class CombinationValidator:
    def is_valid(self, cards):
        # Implement logic to validate card combinations
        if self.is_single(cards) or self.is_pair(cards) or self.is_straight(cards):
            return True
        # Add more checks for other combinations like triples, full houses, bombs, etc.
        return False
    def is_single(self, cards):
        return len(cards) == 1
    def is_pair(self, cards):
        return len(cards) == 2 and cards[0].rank == cards[1].rank
    def is_straight(self, cards):
        # Implement logic to check if cards form a straight
        if len(cards) < 5:
            return False
        sorted_cards = sorted(cards, key=lambda card: card.rank)
        for i in range(len(sorted_cards) - 1):
            if sorted_cards[i+1].rank != sorted_cards[i].rank + 1:
                return False
        return True
    # Additional methods for other combinations can be added here