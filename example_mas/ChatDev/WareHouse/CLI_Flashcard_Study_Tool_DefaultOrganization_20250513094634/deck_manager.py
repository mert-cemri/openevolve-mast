'''
Handles deck-related operations.
'''
class DeckManager:
    def __init__(self, flashcard_manager):
        self.decks = {}
        self.flashcard_manager = flashcard_manager
    def create_deck(self, deck_name):
        if deck_name not in self.decks:
            self.decks[deck_name] = []
            return True
        return False
    def get_decks(self):
        return list(self.decks.keys())