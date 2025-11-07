'''
Handles flashcard-related operations.
'''
class FlashcardManager:
    def __init__(self):
        self.flashcards = {}
    def add_flashcard(self, deck_name, question, answer):
        if deck_name not in self.flashcards:
            self.flashcards[deck_name] = []
        if question is not None and answer is not None:
            self.flashcards[deck_name].append((question, answer))
    def get_flashcards(self, deck_name):
        return self.flashcards.get(deck_name, [])