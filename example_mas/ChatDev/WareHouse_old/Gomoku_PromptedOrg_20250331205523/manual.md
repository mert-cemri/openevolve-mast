manual.md

```
# Gomoku Game

A simple and interactive Gomoku game implemented in Python. Gomoku, also known as Five in a Row, is a strategic board game traditionally played with Go pieces (black and white stones) on a 15x15 board. The objective is to be the first player to form an unbroken row of five stones horizontally, vertically, or diagonally.

---

## 🚀 Features

- Standard 15x15 Gomoku board.
- Two-player interactive gameplay.
- Automatic win detection.
- Clear and intuitive command-line interface.
- Input validation and error handling.

---

## 📋 Requirements

This Gomoku game is implemented entirely in Python and does not require any external dependencies.

### Python Version

- Python 3.x (recommended Python 3.6 or later)

---

## ⚙️ Installation

### Step 1: Clone the Repository

Clone the repository or download the source code files (`gomoku.py` and `main.py`) to your local machine.

```bash
git clone <repository-url>
cd <repository-directory>
```

Alternatively, manually download and save the provided files (`gomoku.py` and `main.py`) into a dedicated directory.

### Step 2: Set Up the Environment

Since there are no external dependencies, you only need Python installed on your system. Verify your Python installation by running:

```bash
python --version
```

If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

---

## 🎮 How to Play

### Starting the Game

Navigate to the directory containing the game files and run the following command:

```bash
python main.py
```

### Gameplay Instructions

1. **Game Start**: The game begins with Player B (Black stones) making the first move.
2. **Making a Move**: Players alternate turns placing their stones on the board. To place a stone, enter the row and column numbers separated by a space when prompted.

Example input:

```
Enter row and column (separated by space): 7 7
```

3. **Rules**:
   - You cannot place a stone on an occupied cell.
   - Moves must be within the bounds of the 15x15 board (rows and columns numbered from 0 to 14).

4. **Winning the Game**: The first player to form an unbroken row of five stones horizontally, vertically, or diagonally wins the game.

5. **Draw Condition**: If all cells are occupied and no player has formed a row of five stones, the game ends in a draw.

---

## 📖 Game Interface

The game board is displayed in the terminal after each move. The board uses the following symbols:

- `.` : Empty cell
- `B` : Black stone (Player B)
- `W` : White stone (Player W)

Example of the board display:

```
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
 0  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 1  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 2  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 3  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 4  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 5  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 6  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 7  .  .  .  .  .  .  .  B  .  .  .  .  .  .  .
 8  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
 9  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
10  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
11  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
12  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
13  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
14  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

---

## 🛠️ Troubleshooting

- **Invalid Input**: If you enter invalid coordinates or non-integer values, the game will prompt you to re-enter valid coordinates.
- **Occupied Cell**: If you attempt to place a stone on an already occupied cell, you will be prompted to choose another cell.
- **Out of Bounds**: If you enter coordinates outside the 0-14 range, you will be prompted to enter valid coordinates.

---

## 📌 Support

For any issues, questions, or suggestions, please contact our support team or open an issue in the project's repository.

Enjoy playing Gomoku!

```