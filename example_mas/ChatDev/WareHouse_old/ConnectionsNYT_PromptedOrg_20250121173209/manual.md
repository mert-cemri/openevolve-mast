# Puzzle Game User Manual

Welcome to the Puzzle Game! This interactive application challenges you to group sixteen words into four categories of four words each. The game follows the standard logic of the NYT Connections game. Your objective is to correctly identify all four categories before running out of tries.

## Main Functions of the Software

- **Interactive Gameplay**: Engage in a fun and challenging word puzzle where you must group words into their respective categories.
- **Feedback System**: After each guess, receive immediate feedback on whether the chosen words form a valid group.
- **Limited Attempts**: You have a limited number of tries to solve the puzzle, adding an element of strategy and excitement.
- **Victory and Defeat Conditions**: The game ends when you successfully form all four correct groups or exhaust all your attempts.

## Installation

This application is developed in Python and does not require any external dependencies. To get started, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the source code from the repository.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the main script to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to begin the game. You will see a shuffled list of words displayed on the screen.

2. **Make a Guess**: Enter four words separated by commas to form a group. Ensure the words are from the displayed list.

3. **Receive Feedback**: After each guess, the game will inform you if the group is correct or incorrect. If correct, those words will be removed from the list.

4. **Continue Guessing**: Keep guessing until you form all four correct groups or run out of tries. You have a total of 10 attempts.

5. **Win or Lose**: The game ends when you successfully identify all categories or use up all your attempts. If you solve the puzzle, you'll receive a congratulatory message. Otherwise, you'll be encouraged to try again.

## Example

Here's a quick example of how the game might proceed:

- **Current Words**: apple, banana, orange, grape, red, blue, green, yellow, cat, dog, lion, tiger, usa, canada, mexico, brazil
- **Guess**: apple, banana, orange, grape
  - **Feedback**: Correct group!
- **Remaining Words**: red, blue, green, yellow, cat, dog, lion, tiger, usa, canada, mexico, brazil

Continue this process until all words are correctly grouped.

## Conclusion

Enjoy the challenge of the Puzzle Game and test your word association skills! If you have any questions or need further assistance, feel free to reach out to our support team. Happy puzzling!