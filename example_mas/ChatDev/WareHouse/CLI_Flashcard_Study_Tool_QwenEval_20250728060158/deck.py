'''
Deck class to represent a collection of flashcards.
'''
from flashcard import Flashcard
class Deck:
    def __init__(self, name):
        self.name = name
        self.flashcards = []
    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)
    def remove_flashcard(self, index):
        if 0 <= index < len(self.flashcards):
            del self.flashcards[index]
    def get_flashcard(self, index):
        if 0 <= index < len(self.flashcards):
            return self.flashcards[index]
        return None
    def __str__(self):
        return f"Deck(name='{self.name}', flashcards={self.flashcards})"