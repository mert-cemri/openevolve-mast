# Hangman Game User Manual

Welcome to the Hangman Game! This classic word-guessing game challenges you to guess a secret word one letter at a time. You have a limited number of attempts, so choose wisely!

## Main Functions

The Hangman Game application includes the following main functions:

- **Random Word Selection**: The game selects a random word from a predefined dictionary.
- **Letter Guessing**: Players can guess letters to uncover the secret word.
- **Tracking Guesses**: The game tracks both correct and incorrect guesses.
- **Game Over Conditions**: The game ends when the player either guesses the word correctly or exhausts all attempts.
- **Graphical User Interface (GUI)**: The game features a user-friendly interface for easy interaction.

## Installation

### Environment Setup

The Hangman Game is developed in Python and requires no external dependencies. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Download the game files from the repository or copy the provided code into your local development environment.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory containing the game files.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Launch the game by running `main.py`. A window will open displaying the Hangman Game interface.

2. **Guess a Letter**: Enter a letter in the input field and click the "Guess" button. The game will reveal the letter's position in the word if it's correct, or add it to the list of incorrect guesses.

3. **Win or Lose**: The game ends when you either guess all the letters in the word or use up all your attempts. A message will display the result.

4. **Restart**: To play again, restart the application.

## Game Interface

- **Word Display**: Shows the current state of the word with placeholders for unguessed letters.
- **Input Field**: Enter your letter guesses here.
- **Guess Button**: Submit your guess.
- **Incorrect Guesses**: Displays the letters you have guessed incorrectly.
- **Result Message**: Informs you of the game's outcome.

Enjoy playing the Hangman Game and test your word-guessing skills!