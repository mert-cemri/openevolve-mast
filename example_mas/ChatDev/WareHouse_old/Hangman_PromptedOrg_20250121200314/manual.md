# Hangman Game

Welcome to the classic Hangman game, a simple yet engaging word-guessing game. This application is designed to provide an interactive experience where you can test your vocabulary and guessing skills.

## Main Functions

The Hangman game includes the following main functions:

- **Random Word Selection**: The game selects a random word from a predefined list of words.
- **User Interaction**: Players guess letters to uncover the hidden word.
- **Feedback on Guesses**: The game provides feedback on whether the guessed letter is correct or incorrect.
- **Attempts Tracking**: The game tracks the number of incorrect guesses and limits the attempts to a maximum of 6.
- **Game Over Conditions**: The game ends when the player either guesses the word correctly or exhausts all attempts.

## Installation

To run the Hangman game, you need to have Python installed on your system. Follow the steps below to set up the environment and run the game:

1. **Install Python**: If you haven't already, download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the Hangman game code to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

4. **Install Dependencies**: The Hangman game does not require any external Python packages, so no additional dependencies need to be installed.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.

   ```bash
   python main.py
   ```

2. **Game Instructions**: Once the game starts, you will see a welcome message and the current word displayed as underscores representing each letter.

3. **Make a Guess**: Enter a single alphabetic character as your guess. The game will inform you if your guess is correct or incorrect.

4. **Track Your Progress**: The game will display the current state of the word with correctly guessed letters revealed and the number of attempts remaining.

5. **Win or Lose**: The game ends when you either guess the entire word correctly or use up all your attempts. A congratulatory message will appear if you win, or the correct word will be revealed if you lose.

Enjoy playing the Hangman game and challenge yourself to guess the word with the fewest attempts possible!