manual.md

```
# Checkers Game (Draughts)

A simple yet comprehensive Checkers (Draughts) game implemented in Python, providing an interactive command-line interface for two players. The game strictly follows standard Checkers rules, including mandatory captures, multiple sequential captures, and kinging.

---

## 🎲 Game Features

- **Standard 8x8 Checkers Board:** A classic Checkers board layout with clearly marked rows (1-8) and columns (a-h).
- **Two-Player Gameplay:** Alternate turns between two players (White and Black).
- **Mandatory Capture Enforcement:** Players must perform captures when available.
- **Multiple Sequential Captures:** If a capture leads to another possible capture, the player must continue capturing with the same piece.
- **Kinging:** Pieces reaching the opposite side of the board become kings, allowing them to move and capture in both directions.
- **Interactive Command-Line Interface:** Moves are entered using standard Checkers notation (e.g., `b6-a5`).

---

## 📦 Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This project does not require any external Python libraries or dependencies.

However, ensure your Python environment is correctly set up:

```bash
python --version
```

### Downloading the Game

Clone or download the game files (`main.py`, `board.py`, and `piece.py`) to your local machine.

```bash
git clone <repository-url>
cd <repository-folder>
```

---

## 🚀 Running the Game

Navigate to the directory containing the game files and execute the following command:

```bash
python main.py
```

---

## 🎮 How to Play

### Starting the Game

Upon running the game, the board will be displayed in the terminal, and the first player (White) will be prompted to make a move.

### Understanding the Board

The board is displayed with rows numbered from bottom (1) to top (8) and columns labeled from left (a) to right (h). Pieces are represented as follows:

- `w`: White piece
- `b`: Black piece
- `W`: White king
- `B`: Black king
- `.`: Empty square

Example board display:

```
  a b c d e f g h
8 . b . b . b . b 
7 b . b . b . b . 
6 . b . b . b . b 
5 . . . . . . . . 
4 . . . . . . . . 
3 w . w . w . w . 
2 . w . w . w . w 
1 w . w . w . w . 
```

### Making Moves

Moves are entered using standard Checkers notation in the format:

```
<from_position>-<to_position>
```

For example, to move a piece from position `b6` to `a5`, enter:

```
b6-a5
```

- Columns are labeled `a` through `h` from left to right.
- Rows are numbered `1` through `8` from bottom to top.

### Capturing Pieces

- If a capture is available, you must perform it.
- Captures are performed by jumping over an opponent's piece to an empty square immediately beyond it.
- If multiple captures are possible, you must continue capturing with the same piece until no further captures are available.

### Kinging Pieces

- When a piece reaches the farthest row from its starting position (row 8 for White, row 1 for Black), it becomes a king.
- Kings can move and capture in both forward and backward directions.

---

## 🏆 Winning the Game

The game continues until one player has no remaining pieces or no valid moves left. The player with remaining pieces or available moves is declared the winner.

---

## 📌 Example Gameplay

```
Player W's turn (e.g., b6-a5):
b6-a5

Player B's turn (e.g., c3-d4):
c3-d4

Capture move available! You must perform a capture.
Player W's turn (e.g., a5-c3):
a5-c3
```

---

## 📚 Support & Feedback

For any questions, issues, or feedback, please contact our support team or open an issue in the project's repository.

Enjoy playing Checkers!

--- 

© 2023 ChatDev - Changing the digital world through programming.
```