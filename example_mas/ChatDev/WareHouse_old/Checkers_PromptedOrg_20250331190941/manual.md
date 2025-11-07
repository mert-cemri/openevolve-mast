manual.md

```
# Checkers (Draughts) Game

A classic Checkers (Draughts) game implemented in Python, providing an interactive command-line interface for two players. This software allows players to experience the traditional 8x8 Checkers game, complete with standard capture and kinging rules.

## 🎲 Game Features

- **Interactive Gameplay**: Two-player alternating turns.
- **Standard Rules**: Implements standard Checkers rules including captures and kinging.
- **Multiple Sequential Captures**: Supports multiple sequential captures in a single turn.
- **Simple Notation**: Players input moves using a straightforward notation (e.g., `5,0-4,1`).

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Installation

1. **Clone the repository** or download the provided files (`piece.py`, `board.py`, `main.py`, `example_move.py`):

```bash
git clone <repository-url>
cd <repository-directory>
```

*(Replace `<repository-url>` and `<repository-directory>` with the actual URL and directory name.)*

2. **Install Dependencies**

This project does not require any external dependencies. However, ensure your Python environment is correctly set up.

```bash
pip install -r requirements.txt
```

*(Note: The provided `requirements.txt` file is empty, as no external dependencies are required.)*

## 🎮 How to Play

### Starting the Game

Run the game by executing the `main.py` script:

```bash
python main.py
```

### Understanding the Board

The board is displayed in an 8x8 grid format with rows and columns numbered from 0 to 7:

- `W` represents a White piece.
- `B` represents a Black piece.
- `WK` or `BK` represents a Kinged piece.
- `.` represents an empty square.

Example board visualization:

```
  0 1 2 3 4 5 6 7
0 . B . B . B . B 
1 B . B . B . B . 
2 . B . B . B . B 
3 . . . . . . . . 
4 . . . . . . . . 
5 W . W . W . W . 
6 . W . W . W . W 
7 W . W . W . W . 
```

### Making a Move

Moves are entered using the notation `from_row,from_col-to_row,to_col`. For example, to move a piece from position `(5,0)` to `(4,1)`, input:

```
5,0-4,1
```

### Capturing Pieces

To capture an opponent's piece, jump over it diagonally to an empty square immediately beyond it. For example, if your piece is at `(5,0)` and an opponent's piece is at `(4,1)`, you can capture it by moving to `(3,2)`:

```
5,0-3,2
```

### Multiple Sequential Captures

If after capturing a piece, another capture is possible with the same piece, you must continue capturing. The game will prompt you to continue capturing with the same piece until no further captures are possible.

### Kinging a Piece

When a piece reaches the farthest row from its starting position (row `0` for White, row `7` for Black), it becomes a King (`WK` or `BK`). Kings can move and capture in both forward and backward diagonal directions.

### Winning the Game

The game continues until one player has no remaining pieces. The player with remaining pieces is declared the winner.

## 📌 Example Move

To see an example of a valid move notation, run the provided `example_move.py` script:

```bash
python example_move.py
```

Output:

```
5,0-4,1
```

## 📖 File Structure

- `piece.py`: Defines the `Piece` class representing individual checker pieces.
- `board.py`: Manages the game state, validates moves, and handles game logic.
- `main.py`: Main executable script implementing the game loop and user interaction.
- `example_move.py`: Demonstrates valid move notation.
- `requirements.txt`: Lists external dependencies (currently none required).

## 🛠️ Troubleshooting

- **Invalid Input**: Ensure your move notation is correct (`row,col-row,col`) and within bounds (`0-7`).
- **Invalid Move**: Moves must follow Checkers rules. Ensure you are moving diagonally, capturing correctly, and following kinging rules.

## 📞 Support

For further assistance or to report issues, please contact our support team or open an issue in the project's repository.

Enjoy your game of Checkers! 🎉
```