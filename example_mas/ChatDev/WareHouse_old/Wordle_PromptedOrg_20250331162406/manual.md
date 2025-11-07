# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation, setup, and gameplay of the Wordle game designed to be played from the Linux Terminal.

## Introduction

The Wordle Game is a terminal-based word puzzle game where the player has to guess a daily 5-letter English word. The player is given 6 attempts to guess the word correctly. After each guess, feedback is provided for each letter: 
- **Green**: Correct letter in the correct position.
- **Yellow**: Correct letter in the wrong position.
- **Grey**: Invalid letter.

## Main Functions

- **WordleGame Class**: Handles the game logic, including word selection, guess validation, and feedback generation.
- **check_guess**: Compares the player's guess with the daily word and provides feedback.
- **is_valid_word**: Validates if the guessed word is a valid 5-letter word from the word list.
- **get_daily_word**: Returns the daily word for testing purposes.

## Installation

### Prerequisites

- Ensure you have Python installed on your Linux system. You can verify this by running `python --version` or `python3 --version` in your terminal.

### Quick Install

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: 
   The game does not require any external Python packages, so no additional dependencies are needed.

## How to Play

1. **Start the Game**:
   Navigate to the directory where the game files are located and run the following command:
   ```bash
   python main.py
   ```

2. **Gameplay**:
   - You will be prompted to guess a 5-letter word.
   - Enter your guess and press Enter.
   - You will receive feedback for each letter in your guess.
   - Continue guessing until you either guess the word correctly or exhaust all 6 attempts.

3. **Winning the Game**:
   - If you guess the word correctly within the allowed attempts, a congratulatory message will be displayed.

4. **Losing the Game**:
   - If you fail to guess the word within 6 attempts, the correct word will be revealed.

## Example

```bash
Welcome to Wordle! Guess the 5-letter word.
Attempt 1/6: apple
Feedback: ['grey', 'grey', 'yellow', 'grey', 'grey']
Attempt 2/6: berry
Feedback: ['grey', 'green', 'grey', 'grey', 'grey']
Attempt 3/6: charm
Feedback: ['green', 'green', 'green', 'green', 'green']
Congratulations! You've guessed the word correctly.
```

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

Enjoy playing Wordle and challenge yourself daily with new words!