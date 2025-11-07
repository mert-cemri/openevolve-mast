'''
Deck class representing a collection of flashcards.
'''
class Deck:
    def __init__(self, name):
        self.name = name
        self.flashcards = []
    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)
    def get_flashcards(self):
        return self.flashcards