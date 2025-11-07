manual.md

```
# Terminal Wordle Game

A simple and interactive Wordle game playable directly from your Linux Terminal. Test your vocabulary and guessing skills by attempting to guess the daily 5-letter English word within 6 attempts.

## 🎯 Overview

Terminal Wordle is a command-line implementation of the popular Wordle game. Each day, a new 5-letter English word is randomly selected. Your goal is to guess this word within 6 attempts. After each guess, you'll receive feedback in the form of colored letters:

- 🟩 **Green**: Correct letter in the correct position.
- 🟨 **Yellow**: Correct letter in the wrong position.
- ⬜ **Grey**: Incorrect letter.

If you guess the word correctly within 6 attempts, you win! If not, the correct word will be revealed at the end of the game.

## 🚀 Features

- Daily changing word based on the current date.
- Immediate visual feedback with colored letters.
- Simple and intuitive gameplay directly from your Linux Terminal.
- No external dependencies required.

## 📦 Installation

### Prerequisites

- Python 3.x installed on your Linux system.

You can verify your Python installation by running:

```bash
python3 --version
```

### Clone the Repository

Clone or download the repository containing the game files (`main.py`, `wordle.py`, and `words.py`) to your local machine.

```bash
git clone <repository-url>
cd <repository-directory>
```

### Install Dependencies

This project does not require any external dependencies. However, it is recommended to use a virtual environment for better dependency management.

To create and activate a virtual environment:

```bash
python3 -m venv wordle-env
source wordle-env/bin/activate
```

## 🎮 How to Play

### Start the Game

Run the game directly from your terminal by executing:

```bash
python3 main.py
```

### Gameplay Instructions

1. Upon starting the game, you will see a welcome message and instructions.
2. You have 6 attempts to guess the daily 5-letter English word.
3. Enter your guess and press `Enter`. Your guess must be a valid 5-letter English word from the provided word list.
4. After each guess, you will receive immediate feedback:
   - Letters highlighted in **green** indicate correct letters in the correct positions.
   - Letters highlighted in **yellow** indicate correct letters in incorrect positions.
   - Letters highlighted in **grey** indicate incorrect letters.
5. Continue guessing based on the feedback provided.
6. If you correctly guess the word within 6 attempts, you win! Otherwise, the correct word will be revealed at the end.

### Example Gameplay

```
Welcome to Terminal Wordle!
You have 6 attempts to guess the 5-letter word.

Attempt 1/6: crane
C R A N E
Attempt 2/6: apple
A P P L E
Attempt 3/6: grape
G R A P E
Congratulations! You guessed the word 'GRAPE' correctly!
```

## 📚 Word List

The game uses a predefined list of common 5-letter English words. You can view or modify this list in the `words.py` file.

## 🛠️ Customization

- To add or remove words from the game, edit the `WORD_LIST` in `words.py`.
- To modify the number of allowed attempts, edit the `attempts` variable in `main.py`.

## 🐞 Troubleshooting

- Ensure your terminal supports ANSI color codes for proper color display.
- If you encounter issues, verify that your Python version is 3.x or higher.

## 📖 License

This project is open-source and free to use or modify.

Enjoy playing Terminal Wordle and challenge yourself daily!
```