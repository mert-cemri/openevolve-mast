manual.md

```
# Connect Four Game

A simple and interactive Connect Four game implemented in Python. This game allows two players to compete by alternately placing discs into a seven-column, six-row grid. The objective is to form a horizontal, vertical, or diagonal line of four discs.

## 🎯 Features

- Interactive command-line interface.
- Clear visual representation of the game board.
- Automatic validation of player moves.
- Detection of winning conditions (horizontal, vertical, diagonal).
- Detection of draw conditions when the board is full.
- Easy-to-follow prompts and error messages.

## ⚙️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Setup

1. Clone or download the project files to your local machine.

2. Navigate to the project directory in your terminal or command prompt.

3. Install dependencies (no external dependencies required):

```bash
pip install -r requirements.txt
```

*(Note: This project does not require external dependencies, so the above command will not install any additional packages.)*

## 🚀 How to Play

### Starting the Game

Run the game by executing the following command in your terminal:

```bash
python main.py
```

### Gameplay Instructions

- The game starts with Player X.
- Players alternate turns, choosing a column number (0-6) to drop their disc.
- The disc will occupy the lowest available space in the chosen column.
- After each move, the board updates and displays the current state.
- The game continues until one player forms a line of four discs horizontally, vertically, or diagonally, or until the board is full, resulting in a draw.

### Making Moves

- When prompted, enter the column number (0-6) where you want to place your disc.
- Example:

```
Player X, choose a column (0-6): 3
```

### Winning the Game

- The game automatically checks for a winning condition after each move.
- If a player successfully connects four discs, the game announces the winner and ends.

### Draw Condition

- If all spaces on the board are filled without any player connecting four discs, the game announces a draw.

### Exiting the Game

- To exit the game at any time, press `Ctrl+C`.

## 📂 Project Structure

```
connect-four-game/
├── connect_four.py      # Contains the ConnectFourGame class and game logic
├── main.py              # Main executable file to run the game
└── requirements.txt     # Lists external dependencies (none required)
```

## 🛠️ Code Overview

- `connect_four.py`: Defines the `ConnectFourGame` class, managing the game state, validating moves, checking for wins/draws, and switching players.
- `main.py`: Provides the command-line interface, handles user input, and manages the game loop.

## 📖 Example Gameplay

```
Welcome to Connect Four!

Current Board:
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
  0   1   2   3   4   5   6
Player X, choose a column (0-6): 3

Current Board:
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   |   |   |   |   |
-----------------------------
|   |   |   | X |   |   |   |
-----------------------------
  0   1   2   3   4   5   6
Player O, choose a column (0-6):
```

## 📞 Support

For any questions, issues, or suggestions, please contact our support team or open an issue in the project's repository.

Enjoy playing Connect Four! 🎉
```