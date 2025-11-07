'''
Handles the review process of flashcards.
'''
class ReviewManager:
    def __init__(self, flashcard_manager):
        self.flashcard_manager = flashcard_manager
        self.current_deck = None
        self.current_index = 0
    def start_review(self, deck_name):
        self.current_deck = deck_name
        self.current_index = 0
    def next_card(self):
        if self.current_deck is None:
            return None
        flashcards = self.flashcard_manager.get_flashcards(self.current_deck)
        if self.current_index < len(flashcards):
            card = flashcards[self.current_index]
            self.current_index += 1
            return card
        return None