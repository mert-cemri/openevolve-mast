'''
Main application file for the CLI flashcard study tool.
'''
from deck import Deck
from flashcard import Flashcard
class FlashcardApp:
    def __init__(self):
        self.decks = {}
        self.current_deck = None
        self.current_flashcard_index = 0
        self.is_front = True
    def create_deck(self):
        while True:
            deck_name = input("Enter deck name: ").strip()
            if deck_name:
                if deck_name not in self.decks:
                    self.decks[deck_name] = Deck(deck_name)
                    print(f"Deck '{deck_name}' created.")
                    break
                else:
                    print("Deck name already exists. Please enter a different name.")
            else:
                print("Deck name cannot be empty. Please enter a valid name.")
    def add_flashcard_to_deck(self):
        if not self.decks:
            print("No decks available. Create a deck first.")
            return
        deck_name = input("Enter deck name: ").strip()
        if deck_name in self.decks:
            while True:
                front = input("Enter flashcard front: ").strip()
                back = input("Enter flashcard back: ").strip()
                if front and back:
                    flashcard = Flashcard(front, back)
                    self.decks[deck_name].add_flashcard(flashcard)
                    print("Flashcard added.")
                    break
                else:
                    print("Flashcard front and back cannot be empty. Please enter valid content.")
        else:
            print("Deck not found.")
    def review_deck(self):
        if not self.decks:
            print("No decks available. Create a deck first.")
            return
        deck_name = input("Enter deck name: ").strip()
        if deck_name in self.decks:
            self.current_deck = self.decks[deck_name]
            if not self.current_deck.get_flashcards():
                print("No flashcards in this deck. Add flashcards first.")
                return
            self.current_flashcard_index = 0
            self.is_front = True
            self.show_flashcard()
        else:
            print("Deck not found.")
    def show_flashcard(self):
        if self.current_deck and self.current_deck.get_flashcards():
            flashcard = self.current_deck.get_flashcards()[self.current_flashcard_index]
            text = flashcard.get_front() if self.is_front else flashcard.get_back()
            print(f"Deck: {self.current_deck.name}")
            print(f"Flashcard: {text}")
        else:
            print("No flashcards available.")
    def flip_flashcard(self):
        self.is_front = not self.is_front
        self.show_flashcard()
    def show_next_flashcard(self):
        if self.current_deck and self.current_deck.get_flashcards():
            self.current_flashcard_index = (self.current_flashcard_index + 1) % len(self.current_deck.get_flashcards())
            self.is_front = True
            self.show_flashcard()
    def start(self):
        while True:
            command = input("Enter command (create, add, review, flip, next, quit): ").strip().lower()
            if command == "create":
                self.create_deck()
            elif command == "add":
                self.add_flashcard_to_deck()
            elif command == "review":
                self.review_deck()
            elif command == "flip":
                self.flip_flashcard()
            elif command == "next":
                self.show_next_flashcard()
            elif command == "quit":
                print("Exiting the flashcard study tool.")
                break
            else:
                print("Unknown command. Please try again.")
if __name__ == "__main__":
    app = FlashcardApp()
    app.start()