# Spelling Bee Puzzle

Welcome to the Spelling Bee Puzzle application! This interactive game challenges you to form words using a central letter and six surrounding letters. The goal is to create as many valid words as possible, each including the central letter at least once. Your score is based on the length of the words you form.

## Quick Install

This application is built using Python and does not require any external dependencies. To get started, ensure you have Python installed on your system.

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application:**
   ```bash
   python main.py
   ```

## 🤔 What is this?

The Spelling Bee Puzzle is a word game where you are provided with one central letter and six surrounding letters. Your task is to form valid words that include the central letter at least once and use only the given letters. The game tracks your score based on the length of the words you create.

### Main Functions of the Software

- **Word Validation:** Ensures that each word includes the central letter, uses only the provided letters, and is present in the dictionary.
- **Scoring System:** Awards points based on the length of the words:
  - 4 letters: 1 point
  - 5 letters: 2 points
  - 6 letters: 3 points
  - 7 letters: 5 points
  - 8 or more letters: 11 points
- **User Feedback:** Provides immediate feedback on the validity and score of each word entered.

## 📖 How to Use/Play

1. **Start the Game:**
   - Run the `main.py` file to start the game.
   - You will see a welcome message and instructions on how to play.

2. **Enter Words:**
   - Type words using the central letter and surrounding letters.
   - Press `Enter` to submit each word.
   - Type 'exit' to quit the game.

3. **Receive Feedback:**
   - After submitting a word, you will receive feedback on its validity and the points earned.
   - Invalid words will prompt a message to try again.

4. **End the Game:**
   - Type 'exit' to end the game session.

## Example

- **Central Letter:** e
- **Surrounding Letters:** a, b, c, d, f, g

Try forming words like "bead", "badge", "cage", etc., using the central letter 'e' and the surrounding letters.

Enjoy playing the Spelling Bee Puzzle and challenge yourself to find as many words as possible!