# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation, setup, and gameplay of the Wordle game designed to be played in the Linux Terminal. This game challenges you to guess a daily 5-letter English word within six attempts, providing feedback on each guess.

## Main Functions

- **Word Guessing**: The primary objective is to guess a 5-letter word within six attempts.
- **Feedback System**: After each guess, feedback is provided:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter in the wrong position.
  - **Grey**: Incorrect letter.
- **Game Over Conditions**: The game ends when the word is guessed correctly or when all six attempts are used.

## Installation

To play the Wordle game, you need to have Python installed on your system. Additionally, the game requires the `colorama` package for color-coded feedback in the terminal.

### Step-by-Step Installation

1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install `colorama`**: Use pip to install the required package.
   ```bash
   pip install colorama
   ```

3. **Download the Game Code**: Save the provided `main.py` script to your local machine.

## How to Play

1. **Start the Game**: Open your terminal and navigate to the directory where `main.py` is located. Run the game using the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions**: Upon starting, you will be greeted with a welcome message and instructions.

3. **Enter Your Guess**: Type a 5-letter word and press Enter. Ensure your guess is a valid English word.

4. **Receive Feedback**: After each guess, observe the color-coded feedback:
   - **Green**: Letter is correct and in the correct position.
   - **Yellow**: Letter is correct but in the wrong position.
   - **Grey**: Letter is not in the word.

5. **Win or Lose**: If you guess the word correctly within six attempts, you win! Otherwise, the correct word will be revealed after six incorrect attempts.

## Example Gameplay

```plaintext
Welcome to Wordle!
You have 6 attempts to guess the 5-letter word.
Enter your guess: apple
Feedback: [Grey] [Grey] [Yellow] [Grey] [Green]
Enter your guess: peach
Feedback: [Green] [Grey] [Grey] [Grey] [Green]
...
Congratulations! You've guessed the word!
```

## Troubleshooting

- **Invalid Input**: Ensure your guess is exactly 5 letters and consists of alphabetic characters only.
- **Installation Issues**: Verify that Python and `colorama` are correctly installed.

Enjoy the challenge of Wordle and improve your word-guessing skills! If you encounter any issues or have feedback, please reach out to our support team.