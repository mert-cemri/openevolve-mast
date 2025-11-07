manual.md

```
# Terminal Chess Game

A fully-featured chess game playable directly from your Linux terminal. Enjoy classic chess gameplay, including advanced features such as castling, en passant, pawn promotion, and automatic enforcement of check and checkmate rules.

---

## 🎯 Features

- **Two-player gameplay**: Play chess directly from your terminal with a friend.
- **Standard chess rules**: Includes castling, en passant, and pawn promotion.
- **Check and Checkmate detection**: Automatically detects and announces checkmate and stalemate conditions.
- **Terminal-based interface**: No GUI required, play entirely within your Linux terminal.

---

## 📦 Installation

### Prerequisites

- Python 3.x installed on your Linux system.

### Step-by-Step Installation

1. **Clone or download the project files** to your local machine.

2. **Navigate to the project directory**:
```bash
cd path/to/your/chess-game-directory
```

3. **Install dependencies** (no external dependencies required, but ensure Python is installed):
```bash
pip install -r requirements.txt
```

*(Note: The provided `requirements.txt` file currently has no external dependencies. This step ensures compatibility for future updates.)*

---

## 🚀 Running the Game

To start playing, simply run the following command from your terminal:

```bash
python main.py
```

---

## 🎮 How to Play

### Board Layout

The chessboard is displayed in the terminal using standard chess notation:

```
8 r n b q k b n r
7 p p p p p p p p
6 . . . . . . . .
5 . . . . . . . .
4 . . . . . . . .
3 . . . . . . . .
2 P P P P P P P P
1 R N B Q K B N R
  a b c d e f g h
```

- Uppercase letters represent white pieces, lowercase letters represent black pieces.
- `.` represents an empty square.

### Making Moves

Moves are entered using standard algebraic notation. Examples:

- Move a pawn from e2 to e4:
```
e2e4
```

- Castling kingside (short castling):
```
O-O
```

- Castling queenside (long castling):
```
O-O-O
```

- Pawn promotion (promote pawn at e7 to Queen at e8):
```
e7e8Q
```

### Gameplay Flow

- The game alternates turns between White and Black.
- After each move, the updated board is displayed.
- The game automatically checks for valid moves, checks, checkmate, and stalemate conditions.
- If an invalid move is entered, the game will prompt you to try again.

### Ending the Game

- The game ends automatically when a checkmate or stalemate is detected.
- The winner or draw condition is announced clearly in the terminal.

---

## 📚 Game Rules and Special Moves

### Castling

- Allowed only if neither the king nor the rook has moved.
- No pieces between the king and rook.
- The king cannot castle through, into, or out of check.

### En Passant

- Special pawn capture available immediately after an opponent's pawn moves two squares forward from its starting position and lands beside your pawn.

### Pawn Promotion

- When a pawn reaches the opposite end of the board, it can be promoted to a Queen, Rook, Bishop, or Knight.

---

## 🛠️ Troubleshooting

- Ensure you have Python 3.x installed by running:
```bash
python --version
```

- If you encounter any unexpected behavior, verify your move notation and ensure it follows the provided examples.

---

## 📞 Support

For any issues, questions, or feature requests, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy your game! ♟️
```