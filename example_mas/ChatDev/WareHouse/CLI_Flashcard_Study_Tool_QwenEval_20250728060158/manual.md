# Flashcard Study Tool CLI

## Quick Install

To install the Flashcard Study Tool CLI, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. If you have `git` installed, you can clone the repository using the following command:

```bash
git clone https://github.com/your-repository/flashcard-study-tool.git
cd flashcard-study-tool
```

If you don't have `git`, you can download the source code as a ZIP file from the repository and extract it to a directory of your choice.

Next, you need to install the required dependencies. This tool does not have any external dependencies, so you can directly run the application.

## 🤔 What is this?

The Flashcard Study Tool CLI is a command-line interface (CLI) application designed to help you create and review flashcards for studying. It allows you to create decks of flashcards, add flashcards to those decks, and review the flashcards in a random order to enhance your memory retention.

## 📖 Documentation

### Main Functions

1. **Create Deck**: You can create a new deck of flashcards by selecting the "Create Deck" option from the main menu. You will be prompted to enter a name for the deck.

2. **Add Flashcard to Deck**: You can add a new flashcard to an existing deck by selecting the "Add Flashcard to Deck" option from the main menu. You will be prompted to choose a deck and then enter the front (question/term) and back (answer/definition) of the flashcard.

3. **Review Flashcards**: You can review the flashcards in a selected deck by selecting the "Review Flashcards" option from the main menu. The flashcards will be presented in a random order. You can press Enter to see the answer and mark the flashcard as known or unknown based on your recall.

4. **Exit**: You can exit the application by selecting the "Exit" option from the main menu.

### How to Use/Play

1. **Run the Application**: Open a terminal or command prompt and navigate to the directory where the source code is located. Run the application using the following command:

   ```bash
   python main.py
   ```

2. **Main Menu**: You will see the main menu with the following options:

   ```
   Flashcard Study Tool
   1. Create Deck
   2. Add Flashcard to Deck
   3. Review Flashcards
   4. Exit
   Enter your choice:
   ```

3. **Create Deck**: Enter `1` to create a new deck. You will be prompted to enter a name for the deck.

4. **Add Flashcard to Deck**: Enter `2` to add a new flashcard to an existing deck. You will be prompted to choose a deck and then enter the front and back of the flashcard.

5. **Review Flashcards**: Enter `3` to review the flashcards in a selected deck. The flashcards will be presented in a random order. You can press Enter to see the answer and mark the flashcard as known or unknown based on your recall.

6. **Exit**: Enter `4` to exit the application.

### Example Workflow

1. **Create a Deck**:
   ```
   Flashcard Study Tool
   1. Create Deck
   2. Add Flashcard to Deck
   3. Review Flashcards
   4. Exit
   Enter your choice: 1
   Enter deck name: Python Basics
   Deck 'Python Basics' created.
   ```

2. **Add Flashcards**:
   ```
   Flashcard Study Tool
   1. Create Deck
   2. Add Flashcard to Deck
   3. Review Flashcards
   4. Exit
   Enter your choice: 2
   1. Python Basics
   Choose a deck number: 1
   Enter front (question/term): What is a list in Python?
   Enter back (answer/definition): A list in Python is an ordered collection of items that can be of different types.
   Flashcard added.
   ```

3. **Review Flashcards**:
   ```
   Flashcard Study Tool
   1. Create Deck
   2. Add Flashcard to Deck
   3. Review Flashcards
   4. Exit
   Enter your choice: 3
   1. Python Basics
   Choose a deck number: 1
   Flashcard 1: What is a list in Python?
   Press Enter to see the answer... (or type 'exit' to quit review)
   Answer: A list in Python is an ordered collection of items that can be of different types.
   Was this correct? (y/n): y
   Review Summary:
   Known Flashcards: 1
   Unknown Flashcards: 0
   ```

4. **Exit**:
   ```
   Flashcard Study Tool
   1. Create Deck
   2. Add Flashcard to Deck
   3. Review Flashcards
   4. Exit
   Enter your choice: 4
   Exiting...
   ```

## 🛠️ Development

If you want to contribute to the development of the Flashcard Study Tool CLI, you can clone the repository and make changes to the source code. You can then submit a pull request with your changes.

## 🙏 Acknowledgments

We would like to thank the open-source community for their contributions and support.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This manual should provide a comprehensive guide for users to understand and use the Flashcard Study Tool CLI effectively.