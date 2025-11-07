# Flashcard CLI Study Tool

Welcome to the Flashcard CLI Study Tool! This tool allows you to create decks of flashcards, add flashcards to those decks, and review them through a command-line interface. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it effectively.

## Quick Install

This project does not require any external dependencies, so you can run it directly with Python. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Main Functions

The Flashcard CLI Study Tool provides the following main functions:

- **Create Deck**: Allows you to create a new deck of flashcards.
- **Add Flashcard**: Enables you to add a new flashcard to an existing deck.
- **Review Deck**: Lets you review the flashcards in a specific deck.
- **Flip Flashcard**: Flips the current flashcard to show either the front or the back.
- **Next Flashcard**: Moves to the next flashcard in the deck.
- **Quit**: Exits the application.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file using Python.

   ```bash
   python main.py
   ```

3. **Commands**: Once the application is running, you can use the following commands:

   - **Create a Deck**: Type `create` and follow the prompts to enter a deck name.
   - **Add a Flashcard**: Type `add` and follow the prompts to select a deck and enter the front and back of the flashcard.
   - **Review a Deck**: Type `review` and follow the prompts to select a deck for review.
   - **Flip a Flashcard**: Type `flip` to flip the current flashcard.
   - **Next Flashcard**: Type `next` to move to the next flashcard in the deck.
   - **Quit**: Type `quit` to exit the application.

## Example Usage

Here's a quick example of how you might interact with the tool:

1. Start the application:

   ```bash
   python main.py
   ```

2. Create a new deck:

   ```
   Enter command (create, add, review, flip, next, quit): create
   Enter deck name: Biology
   Deck 'Biology' created.
   ```

3. Add a flashcard to the deck:

   ```
   Enter command (create, add, review, flip, next, quit): add
   Enter deck name: Biology
   Enter flashcard front: What is the powerhouse of the cell?
   Enter flashcard back: Mitochondria
   Flashcard added.
   ```

4. Review the deck:

   ```
   Enter command (create, add, review, flip, next, quit): review
   Enter deck name: Biology
   Deck: Biology
   Flashcard: What is the powerhouse of the cell?
   ```

5. Flip the flashcard:

   ```
   Enter command (create, add, review, flip, next, quit): flip
   Deck: Biology
   Flashcard: Mitochondria
   ```

6. Move to the next flashcard or quit when done.

## Conclusion

This Flashcard CLI Study Tool is a simple yet effective way to create and review flashcards directly from your command line. We hope this tool enhances your study sessions and helps you retain information more effectively. Enjoy using the Flashcard CLI Study Tool!