'''
Represents a player in the Dou Dizhu game.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def add_card(self, card):
        '''
        Adds a single card to the player's hand.
        '''
        self.hand.append(card)
    def add_cards(self, cards):
        '''
        Adds multiple cards to the player's hand.
        '''
        self.hand.extend(cards)
    def play_cards(self, cards):
        '''
        Plays the specified cards from the player's hand if they are present.
        '''
        if all(card in self.hand for card in cards):
            for card in cards:
                self.hand.remove(card)
            return True
        return False
    def has_won(self):
        '''
        Checks if the player has won by running out of cards.
        '''
        return len(self.hand) == 0
    def __str__(self):
        '''
        Returns a string representation of the player's hand.
        '''
        return f"{self.name}: {' '.join(self.hand)}"