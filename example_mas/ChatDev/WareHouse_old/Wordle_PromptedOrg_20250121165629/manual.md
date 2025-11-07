# Wordle Terminal Game

Welcome to the Wordle Terminal Game! This is a simple, terminal-based version of the popular word-guessing game, Wordle. The objective is to guess a daily 5-letter English word within 6 attempts. Feedback is provided for each guess, indicating correct letters in the correct position, correct letters in the wrong position, and incorrect letters.

## Main Functions

- **Daily Word Generation**: The game generates a new 5-letter word each day using a fixed list of words. The word is selected based on the current date to ensure consistency.
- **Guess Feedback**: After each guess, feedback is provided:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter in the wrong position.
  - **Grey**: Incorrect letter.
- **Attempts**: Players have 6 attempts to guess the word correctly.
- **Color Support**: The game supports colored feedback in terminals that support ANSI colors.

## Installation

### Environment Setup

1. **Python Version**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **No External Dependencies**: The game does not require any external Python packages, so no additional installations are necessary.

### Running the Game

1. **Download the Code**: Save the provided `main.py` file to your local machine.

2. **Execute the Game**: Open your terminal and navigate to the directory where `main.py` is located. Run the game using the following command:

   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Upon running the game, you will be greeted with a welcome message and instructions.

2. **Enter Your Guess**: Type a 5-letter word and press Enter. Ensure your guess is exactly 5 letters long.

3. **Receive Feedback**: After each guess, feedback will be displayed:
   - Letters in green are correct and in the correct position.
   - Letters in yellow are correct but in the wrong position.
   - Letters in grey are incorrect.

4. **Win or Lose**: If you guess the word correctly within 6 attempts, you win! If not, the correct word will be revealed after your 6th attempt.

5. **Play Again**: To play again, simply rerun the `main.py` script.

## Additional Information

- **Color Support**: The game automatically detects if your terminal supports ANSI colors. If not, feedback will be displayed without colors.
- **Daily Word**: The word changes daily based on the current date, ensuring a new challenge each day.

Enjoy playing Wordle in your terminal and challenge yourself to guess the word in as few attempts as possible!