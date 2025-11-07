# Hangman Game User Manual

Welcome to the Hangman Game! This classic word-guessing game challenges you to guess a hidden word by suggesting letters within a limited number of attempts. Enjoy the thrill of solving the puzzle before your attempts run out!

## Main Functions

The Hangman Game consists of the following main functions:

1. **Random Word Selection**: The game selects a random word from a predefined list of words.
2. **Letter Guessing**: Players can guess letters to uncover the hidden word.
3. **State Display**: The game displays the current state of the word with placeholders for unguessed letters.
4. **Attempt Tracking**: The game tracks the number of incorrect guesses and remaining attempts.
5. **Game Over Conditions**: The game ends when the word is completely guessed or when the player runs out of attempts.

## Installation

To play the Hangman Game, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

1. **Install Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Game Directory**: Change your working directory to the game folder:
   ```bash
   cd <repository-folder>
   ```

4. **Run the Game**: Execute the main script to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. You will be greeted with a welcome message.

2. **Guess a Letter**: Enter a single alphabetic character as your guess. The game will inform you if the letter is correct or incorrect.

3. **View Game State**: After each guess, the game displays the current state of the word with placeholders for unguessed letters, the list of incorrect guesses, and the number of attempts left.

4. **Win or Lose**: The game continues until you either guess the entire word correctly or exhaust all your attempts. If you guess the word, you win! If you run out of attempts, the game reveals the word.

5. **Play Again**: Restart the game by running the `main.py` script again.

Enjoy playing the Hangman Game and challenge yourself to guess the word with the fewest attempts possible!