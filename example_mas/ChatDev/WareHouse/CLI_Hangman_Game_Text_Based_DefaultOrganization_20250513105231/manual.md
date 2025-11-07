# Hangman CLI Game

Welcome to the Hangman CLI Game! This is a simple command-line interface game where you can test your word-guessing skills. The game randomly selects a word, and you have to guess it letter by letter. Be careful, as you only have a limited number of incorrect guesses!

## Main Functions

- **Random Word Selection**: The game selects a random word from a predefined list.
- **Letter Guessing**: Players can guess one letter at a time.
- **Display Progress**: The game displays the word with guessed letters filled in and underscores for remaining letters.
- **Track Incorrect Guesses**: The game keeps track of incorrect guesses and displays them.
- **Win/Loss Conditions**: The game ends when the player guesses the word correctly or runs out of allowed incorrect guesses.

## Quick Install

To play the Hangman CLI Game, you need to have Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/).

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/hangman-cli-game.git
cd hangman-cli-game
```

### Step 2: Install Dependencies

This game does not require any external Python packages, so no additional dependencies need to be installed. Just ensure you have Python 3.x installed.

## How to Play

1. **Start the Game**: Run the main application file using Python.

   ```bash
   python main.py
   ```

2. **Gameplay**: 
   - The game will display the word with underscores representing unguessed letters.
   - Enter a single letter to guess.
   - The game will update the display with correctly guessed letters and track incorrect guesses.
   - You have a maximum of 6 incorrect guesses.

3. **Winning the Game**: 
   - If you guess all the letters in the word correctly, you win!
   - The game will display a congratulatory message and reveal the word.

4. **Losing the Game**: 
   - If you reach the maximum number of incorrect guesses, the game ends.
   - The game will display a game over message and reveal the word.

Enjoy playing the Hangman CLI Game and test your word-guessing skills!