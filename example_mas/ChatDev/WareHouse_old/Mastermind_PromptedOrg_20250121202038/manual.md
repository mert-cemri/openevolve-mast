# Mastermind Game

Welcome to the Mastermind Game! This classic code-breaking game challenges you to guess a hidden sequence of colors within a set number of attempts. The game provides feedback on your guesses, helping you to crack the code.

## Quick Install

To get started with the Mastermind Game, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can run the game by following these steps:

1. Clone the repository or download the game files to your local machine.
2. Navigate to the directory containing the game files.
3. Run the game using the following command:

   ```bash
   python main.py
   ```

## Game Overview

The Mastermind Game is a single-player game where the computer selects a hidden sequence of colors, and the player attempts to guess it. After each guess, the game provides feedback on the number of correct colors in the correct position and the number of correct colors in the wrong position.

### Main Functions

- **Generate Code**: The game generates a random sequence of colors as the hidden code. The available colors are Red (R), Green (G), Blue (B), Yellow (Y), Orange (O), and Purple (P).
- **Validate Guess**: The game validates the player's guess to ensure it matches the required format.
- **Provide Feedback**: After each guess, the game provides feedback on the number of correct positions and correct colors.

### How to Play

1. **Start the Game**: Run the game using the command `python main.py`. You will be welcomed to the Mastermind Game.
2. **Understand the Rules**: The game will prompt you to guess a 4-color code using the letters R, G, B, Y, O, P. You have 10 attempts to guess the correct code.
3. **Make a Guess**: Enter your guess when prompted. The guess should be a 4-letter code using the available colors.
4. **Receive Feedback**: After each guess, the game will provide feedback indicating how many colors are in the correct position and how many are correct but in the wrong position.
5. **Win or Lose**: If you guess the correct code within the allowed attempts, you win the game. If you run out of attempts, the game will reveal the hidden code.

## Example

Here's an example of how the game might proceed:

```
Welcome to Mastermind!
Try to guess the 4-color code using the letters R, G, B, Y, O, P.
You have 10 attempts.

Attempt 1: RGBY
Feedback: 1 correct position(s), 2 correct color(s).

Attempt 2: GGRB
Feedback: 2 correct position(s), 1 correct color(s).

...

Congratulations! You've cracked the code!
```

## Troubleshooting

- **Invalid Guess**: If you enter an invalid guess (e.g., incorrect length or invalid characters), the game will prompt you to enter a valid guess.
- **Input Errors**: If an input error occurs, the game will notify you and prompt you to try again.

Enjoy playing the Mastermind Game and challenge yourself to crack the code!