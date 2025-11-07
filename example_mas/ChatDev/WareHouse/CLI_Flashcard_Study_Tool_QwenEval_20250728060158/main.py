'''
Main entry point for the Flashcard Study Tool CLI application.
'''
from app import FlashcardApp
def main():
    app = FlashcardApp()
    app.run()
if __name__ == "__main__":
    main()