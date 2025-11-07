# Hangman Game User Manual

Welcome to the classic Hangman game! This manual will guide you through the installation, setup, and gameplay of the Hangman game developed in Python.

## Introduction

The Hangman game is a word-guessing game where the player attempts to guess a hidden word by suggesting letters within a limited number of attempts. The game provides feedback on correct and incorrect guesses and displays the current state of the word with placeholders for unguessed letters.

## Main Functions

- **Random Word Selection**: The game selects a random word from a predefined list for the player to guess.
- **Guessing Mechanism**: Players can guess letters, and the game will indicate whether the guess is correct or incorrect.
- **Attempts Tracking**: The game tracks the number of incorrect attempts and ends when the player either guesses the word or exhausts all attempts.
- **Game State Display**: The current state of the word is displayed with placeholders for unguessed letters.
- **Result Display**: At the end of the game, a message is displayed indicating whether the player won or lost.

## Installation

To play the Hangman game, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Download the Game Code**: Save the `main.py` file containing the Hangman game code to your local machine.

3. **No Additional Dependencies**: The game does not require any additional Python packages beyond the standard library.

## How to Play

1. **Run the Game**: Open a terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:

   ```
   python main.py
   ```

2. **Game Start**: The game will welcome you to Hangman and select a random word from the list.

3. **Guessing Letters**: You will be prompted to guess a letter. Enter a single alphabetical character and press Enter.

4. **Feedback**: The game will inform you if your guess was correct or incorrect and display the number of attempts remaining.

5. **Game Over**: The game ends when you either guess the entire word or run out of attempts. A message will display the result.

6. **Play Again**: To play again, simply rerun the `main.py` script.

## Example Gameplay

```
Welcome to Hangman!

Current word: _ _ _ _ _ _ _
Guess a letter: p
Good guess! The letter 'p' is in the word.

Current word: p _ _ _ _ _ _
Guess a letter: x
Sorry, the letter 'x' is not in the word. Attempts remaining: 5

...

Congratulations! You've guessed the word 'python'!
```

Enjoy playing Hangman and challenge yourself to guess the word with the fewest incorrect attempts!