# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation and usage of the Wordle game application, which is designed to be played directly from your Linux Terminal.

## Introduction

The Wordle Game is a simple yet engaging word puzzle game where you have to guess a daily 5-letter English word. You have 6 attempts to guess the word correctly. After each guess, you receive feedback on the correctness of each letter in your guess:
- **Green**: The letter is correct and in the correct position.
- **Yellow**: The letter is correct but in the wrong position.
- **Grey**: The letter is not in the word.

## Quick Install

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Download the game code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: The game does not require any external Python packages, so no additional installation is necessary.

## How to Play

1. **Start the Game**: Run the game using the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Game Instructions**: Once the game starts, you will be greeted with a welcome message and instructions.

3. **Make a Guess**: Enter a 5-letter word when prompted. You have 6 attempts to guess the correct word.

4. **Receive Feedback**: After each guess, the game will provide feedback on each letter:
   - **Green**: Correct letter in the correct position.
   - **Yellow**: Correct letter in the wrong position.
   - **Grey**: Incorrect letter.

5. **Win or Lose**: If you guess the word correctly within 6 attempts, you win! If not, the correct word will be revealed after your attempts are exhausted.

## Example Gameplay

```
Welcome to Wordle!
Guess the 5-letter word. You have 6 attempts.
Attempt 1: apple
Feedback: ['grey', 'yellow', 'grey', 'grey', 'grey']
Attempt 2: peach
Feedback: ['green', 'grey', 'grey', 'grey', 'grey']
Attempt 3: grape
Feedback: ['green', 'grey', 'grey', 'grey', 'green']
Attempt 4: grape
Congratulations! You've guessed the word!
```

## Troubleshooting

- **Invalid Input**: Ensure your guess is exactly 5 letters long. The game will prompt you to enter a valid word if your input is incorrect.

- **Python Errors**: Ensure you are using a compatible version of Python. The game is designed to work with Python 3.x.

## Conclusion

Enjoy playing the Wordle Game and challenge yourself to guess the daily word! If you have any questions or need further assistance, please feel free to reach out.

Happy guessing!