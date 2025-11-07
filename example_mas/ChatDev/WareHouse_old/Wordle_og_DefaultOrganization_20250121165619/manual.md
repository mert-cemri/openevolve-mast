# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation and usage of the Wordle game, a terminal-based application that challenges you to guess a five-letter word within six attempts.

## Overview

The Wordle Game is a simple yet engaging word puzzle game where players have six attempts to guess a randomly selected five-letter word. After each guess, feedback is provided to help the player refine their guesses:
- **Green**: Correct letter in the correct position.
- **Yellow**: Correct letter in the wrong position.
- **Grey**: Incorrect letter.

## Installation

### Prerequisites

To run the Wordle Game, you need to have Python installed on your Linux system. You can check if Python is installed by running:

```bash
python --version
```

If Python is not installed, you can install it using your package manager. For example, on Ubuntu, you can use:

```bash
sudo apt update
sudo apt install python3
```

### Downloading the Game

1. Clone the repository or download the `main.py` file to your local machine.

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Ensure you have the necessary permissions to execute the script:

```bash
chmod +x main.py
```

## How to Play

1. Open your terminal and navigate to the directory where `main.py` is located.

2. Run the game using Python:

```bash
python main.py
```

3. Follow the on-screen instructions:

   - You will be prompted to enter a five-letter word as your guess.
   - After each guess, feedback will be provided in the form of colors (printed as text) indicating the accuracy of your guess.
   - You have six attempts to guess the correct word.

4. If you guess the word correctly within the allowed attempts, you win! If not, the correct word will be revealed after your sixth attempt.

## Example Gameplay

```
Welcome to Wordle!
You have 6 attempts to guess the 5-letter word.
Attempt 1: apple
Feedback: ['grey', 'yellow', 'grey', 'grey', 'grey']
Attempt 2: grape
Feedback: ['green', 'grey', 'grey', 'grey', 'green']
Attempt 3: grape
Congratulations! You've guessed the word!
```

## Troubleshooting

- **Invalid Input**: Ensure that your guess is exactly five letters long. The game will prompt you to enter a valid word if your input does not meet this requirement.

- **Python Errors**: If you encounter any Python-related errors, ensure that you have Python 3 installed and that you are running the script with the correct version.

## Conclusion

Enjoy playing the Wordle Game and challenge yourself to guess the word in as few attempts as possible! If you have any questions or need further assistance, feel free to reach out to our support team.