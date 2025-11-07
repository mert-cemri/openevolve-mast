manual.md

```
# Classic Sudoku Puzzle Game

Enjoy the timeless challenge of Sudoku right from your terminal! This classic Sudoku puzzle game provides an interactive experience, allowing you to solve puzzles by filling in numbers on a 9x9 grid. Test your logic and problem-solving skills by ensuring each row, column, and 3x3 subgrid contains the digits 1 through 9 exactly once.

---

## 🚀 Features

- **Interactive Gameplay:** Enter numbers directly into the Sudoku grid via terminal input.
- **Real-time Validation:** Instantly checks for conflicts and invalid moves.
- **Puzzle Completion Check:** Automatically detects when the puzzle is successfully completed.
- **User-friendly Interface:** Clearly displays the Sudoku grid with visual separators for easy readability.

---

## 🛠️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This Sudoku game does not require any external dependencies. However, ensure your Python environment is correctly set up.

To verify your Python installation, open your terminal or command prompt and run:

```bash
python --version
```

You should see output similar to:

```
Python 3.x.x
```

---

## 🎮 How to Play

### Step 1: Download the Game Files

Ensure you have the following files in the same directory:

- `sudoku.py`
- `game.py`
- `main.py`

### Step 2: Run the Game

Navigate to the directory containing the game files in your terminal or command prompt and execute:

```bash
python main.py
```

### Step 3: Gameplay Instructions

Upon running the game, you will see the Sudoku grid displayed in your terminal. Empty cells are represented by dots (`.`).

- **Entering Moves:**  
  You will be prompted to enter your move by specifying:
  - **Row:** Enter a number from 1 to 9 indicating the row.
  - **Column:** Enter a number from 1 to 9 indicating the column.
  - **Number:** Enter a digit from 1 to 9 to place in the selected cell.

Example input:

```
Enter row (1-9): 3
Enter column (1-9): 4
Enter number (1-9): 7
```

- **Validation:**  
  The game automatically checks if your move is valid. If the move conflicts with existing numbers or attempts to modify a pre-filled cell, you will receive an error message and be prompted to try again.

- **Completing the Puzzle:**  
  Continue filling in numbers until the puzzle is complete. The game will automatically detect when the puzzle is correctly solved and congratulate you!

---

## 📖 Game Rules

- Each row must contain the digits 1 through 9 exactly once.
- Each column must contain the digits 1 through 9 exactly once.
- Each 3x3 subgrid (outlined by bold lines) must contain the digits 1 through 9 exactly once.
- You cannot modify cells that are part of the initial puzzle setup.

---

## 🧩 Example Puzzle

The game includes an example puzzle to get you started:

```
-------------------------
| 5 3 . | . 7 . | . . . | 
| 6 . . | 1 9 5 | . . . | 
| . 9 8 | . . . | . 6 . | 
-------------------------
| 8 . . | . 6 . | . . 3 | 
| 4 . . | 8 . 3 | . . 1 | 
| 7 . . | . 2 . | . . 6 | 
-------------------------
| . 6 . | . . . | 2 8 . | 
| . . . | 4 1 9 | . . 5 | 
| . . . | . 8 . | . 7 9 | 
-------------------------
```

---

## 📞 Support & Feedback

Encountered an issue or have suggestions for improvement? We'd love to hear from you! Please reach out to our support team or submit feedback through our official channels.

Enjoy solving Sudoku puzzles and sharpening your mind with our Classic Sudoku Puzzle Game!

--- 

Happy puzzling! 🎉
```