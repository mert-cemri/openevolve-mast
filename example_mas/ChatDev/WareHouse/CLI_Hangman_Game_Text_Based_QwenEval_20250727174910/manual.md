# Hangman CLI Game

Welcome to the Hangman CLI Game! This manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to play the game.

## Quick Install

To install the Hangman CLI Game, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. If you have `git` installed, you can clone the repository using the following command:

```bash
git clone https://github.com/ChatDev/hangman-cli-game.git
cd hangman-cli-game
```

If you don't have `git`, you can download the source code as a ZIP file from the [GitHub repository](https://github.com/ChatDev/hangman-cli-game) and extract it to a directory of your choice.

## 🤔 What is this?

The Hangman CLI Game is a simple command-line interface (CLI) application that allows you to play the classic Hangman game. The game randomly selects a word from a predefined list, and you need to guess the letters to reveal the word. You have a limited number of incorrect guesses before the game is over.

## 📖 Documentation

### Main Functions

1. **Word Selection**: The `WordSelector` class is responsible for selecting a random word from a predefined list stored in `words.txt`.
2. **Game Logic**: The `HangmanGame` class manages the game state, including guessed letters, incorrect guesses, and game status.
3. **CLI Interface**: The `CLIInterface` class handles user input and displays the game state through the command line.

### How to Play

1. **Start the Game**: Navigate to the directory where the source code is located and run the following command:

    ```bash
    python main.py
    ```

2. **Guess Letters**: The game will display the current state of the word with guessed letters filled in and the number of incorrect guesses. Enter a single letter to make a guess.

3. **Game Over**: The game will end when you either guess the word correctly or exceed the maximum number of incorrect guesses (6).

### Example Game Session

```
Welcome to Hangman!
Word: _ _ _ _ _ _ _
Incorrect guesses: 0/6
Guess a letter: p
Correct!
Word: p _ _ _ _ _ _
Incorrect guesses: 0/6
Guess a letter: y
Correct!
Word: p y _ _ _ _ _
Incorrect guesses: 0/6
Guess a letter: t
Incorrect!
Word: p y _ _ _ _ _
Incorrect guesses: 1/6
Guess a letter: h
Incorrect!
Word: p y _ _ _ _ _
Incorrect guesses: 2/6
Guess a letter: o
Incorrect!
Word: p y _ _ _ _ _
Incorrect guesses: 3/6
Guess a letter: n
Incorrect!
Word: p y _ _ _ _ _
Incorrect guesses: 4/6
Guess a letter: a
Incorrect!
Word: p y _ _ _ _ _
Incorrect guesses: 5/6
Guess a letter: m
Incorrect!
Game over! You failed to guess the word: python
```

### Customizing the Word List

You can customize the word list by editing the `words.txt` file. Each word should be on a new line. For example:

```
python
hangman
challenge
programming
developer
```

## 🛠️ Dependencies

This project does not require any third-party dependencies. All necessary modules are included in the Python standard library.

## 🙌 Contributing

We welcome contributions to the Hangman CLI Game! If you have any ideas for improvements or bug fixes, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/hangman-cli-game).

## 📧 Contact

If you have any questions or need support, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy playing Hangman CLI Game!