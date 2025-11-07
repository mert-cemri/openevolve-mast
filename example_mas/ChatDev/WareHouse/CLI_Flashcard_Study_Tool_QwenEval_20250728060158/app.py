'''
FlashcardApp class to manage the overall application flow.
'''
from deck import Deck
from flashcard import Flashcard
import random
class FlashcardApp:
    def __init__(self):
        self.decks = []
    def run(self):
        while True:
            print("\nFlashcard Study Tool")
            print("1. Create Deck")
            print("2. Add Flashcard to Deck")
            print("3. Review Flashcards")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_deck()
            elif choice == '2':
                self.add_flashcard()
            elif choice == '3':
                self.review_flashcards()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    def create_deck(self):
        name = input("Enter deck name: ")
        deck = Deck(name)
        self.decks.append(deck)
        print(f"Deck '{name}' created.")
    def add_flashcard(self):
        if not self.decks:
            print("No decks available. Please create a deck first.")
            return
        for i, deck in enumerate(self.decks):
            print(f"{i + 1}. {deck.name}")
        deck_choice = input("Choose a deck number: ")
        try:
            deck_choice = int(deck_choice) - 1
        except ValueError:
            print("Invalid input. Please enter a valid deck number.")
            return
        if 0 <= deck_choice < len(self.decks):
            front = input("Enter front (question/term): ")
            back = input("Enter back (answer/definition): ")
            flashcard = Flashcard(front, back)
            self.decks[deck_choice].add_flashcard(flashcard)
            print("Flashcard added.")
        else:
            print("Invalid deck choice.")
    def review_flashcards(self):
        '''
        Method to review flashcards in a selected deck.
        Shuffles the flashcards for random review.
        Marks flashcards as known or unknown based on user input.
        Provides a summary of the review at the end.
        '''
        if not self.decks:
            print("No decks available. Please create a deck first.")
            return
        for i, deck in enumerate(self.decks):
            print(f"{i + 1}. {deck.name}")
        deck_choice = input("Choose a deck number: ")
        try:
            deck_choice = int(deck_choice) - 1
        except ValueError:
            print("Invalid input. Please enter a valid deck number.")
            return
        if 0 <= deck_choice < len(self.decks):
            deck = self.decks[deck_choice]
            if not deck.flashcards:
                print("No flashcards in this deck.")
                return
            flashcards = deck.flashcards.copy()
            random.shuffle(flashcards)  # Shuffle flashcards for random review
            known_flashcards = []
            unknown_flashcards = []
            for i, flashcard in enumerate(flashcards):
                print(f"\nFlashcard {i + 1}: {flashcard.front}")
                user_input = input("Press Enter to see the answer... (or type 'exit' to quit review)")
                if user_input.lower() == 'exit':
                    confirm_exit = input("Are you sure you want to exit the review? (y/n): ").strip().lower()
                    if confirm_exit == 'y':
                        print("Exiting review.")
                        break
                else:
                    print(f"Answer: {flashcard.back}")
                    mark = input("Was this correct? (y/n): ").strip().lower()
                    if mark == 'y':
                        known_flashcards.append(flashcard)
                    else:
                        unknown_flashcards.append(flashcard)
            print("\nReview Summary:")
            print(f"Known Flashcards: {len(known_flashcards)}")
            print(f"Unknown Flashcards: {len(unknown_flashcards)}")
        else:
            print("Invalid deck choice.")