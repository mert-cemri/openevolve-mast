'''
Main application file to run the flashcard study tool.
'''
from deck_manager import DeckManager
from flashcard_manager import FlashcardManager
from review_manager import ReviewManager
class FlashcardApp:
    def __init__(self):
        self.flashcard_manager = FlashcardManager()
        self.deck_manager = DeckManager(self.flashcard_manager)
        self.review_manager = ReviewManager(self.flashcard_manager)
    def create_deck(self):
        deck_name = input("Enter the name of the new deck: ")
        if self.deck_manager.create_deck(deck_name):
            print(f"Deck '{deck_name}' created successfully!")
        else:
            print(f"Deck '{deck_name}' already exists.")
    def add_flashcard(self):
        deck_name = input("Enter the name of the deck to add a flashcard to: ")
        if deck_name in self.deck_manager.get_decks():
            question = input("Enter the question/term: ")
            answer = input("Enter the answer/definition: ")
            self.flashcard_manager.add_flashcard(deck_name, question, answer)
            print("Flashcard added successfully!")
        else:
            print("Please select a valid deck.")
    def review_flashcards(self):
        deck_name = input("Enter the name of the deck to review: ")
        if deck_name in self.deck_manager.get_decks():
            self.review_manager.start_review(deck_name)
            while True:
                card = self.review_manager.next_card()
                if card:
                    question, answer = card
                    print(f"Question/Term: {question}")
                    input("Press Enter to see the answer...")
                    print(f"Answer/Definition: {answer}")
                    input("Press Enter to continue...")
                else:
                    print("You have reviewed all flashcards in this deck.")
                    break
        else:
            print("Please select a valid deck.")
    def run(self):
        while True:
            print("\nFlashcard Study Tool")
            print("1. Create Deck")
            print("2. Add Flashcard")
            print("3. Review Flashcards")
            print("4. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.create_deck()
            elif choice == '2':
                self.add_flashcard()
            elif choice == '3':
                self.review_flashcards()
            elif choice == '4':
                print("Exiting the Flashcard Study Tool.")
                break
            else:
                print("Invalid option. Please try again.")
if __name__ == "__main__":
    app = FlashcardApp()
    app.run()