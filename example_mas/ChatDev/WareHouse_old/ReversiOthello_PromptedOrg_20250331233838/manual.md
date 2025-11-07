manual.md

```
# Reversi (Othello) Board Game

Welcome to the Reversi (Othello) Board Game, developed by ChatDev. This software provides an interactive and user-friendly implementation of the classic Reversi game, allowing two players to compete on an 8x8 grid. Players alternate placing discs, flipping the opponent's discs that lie between the newly placed piece and existing pieces of the same color. The game automatically identifies valid moves, flips discs accordingly, and displays the current score.

## 🎯 Main Features

- **Interactive Gameplay:** Two-player interactive gameplay on an 8x8 board.
- **Automatic Move Validation:** Automatically identifies and displays valid moves for each player.
- **Disc Flipping Logic:** Automatically flips opponent's discs according to Reversi rules.
- **Score Tracking:** Real-time score display for both players.
- **Game Termination Detection:** Automatically detects and announces game termination scenarios (board full or no valid moves remaining).
- **Robust Error Handling:** Provides clear feedback and error messages for invalid moves or inputs.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone or Download the Project**

   Clone the repository or download the provided files (`reversi.py`, `main.py`, and `requirements.txt`) to your local machine.

2. **Navigate to the Project Directory**

   Open your terminal or command prompt and navigate to the directory containing the downloaded files.

   ```bash
   cd path/to/reversi-game
   ```

3. **Install Dependencies**

   This project does not require any external dependencies. However, it's good practice to create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   Since there are no external dependencies, you can skip installing from `requirements.txt`.

## 🎮 How to Play

### Starting the Game

Run the game by executing the `main.py` file:

```bash
python main.py
```

### Gameplay Instructions

- The game begins with the initial setup of four discs placed in the center of the board.
- Player 'X' starts the game, followed by player 'O'.
- The game will display the current board state, available valid moves, and the current score after each turn.

### Making a Move

- When prompted, enter your move by specifying the row and column numbers separated by a space. For example, to place a disc at row 2, column 3, type:

  ```
  2 3
  ```

- If you enter an invalid move or input, the game will provide clear feedback and prompt you to try again.

### Game Rules

- You must place your disc in a position that captures at least one of your opponent's discs.
- Capturing occurs when your newly placed disc and another of your discs enclose a straight line (horizontal, vertical, or diagonal) of your opponent's discs.
- All enclosed opponent discs are flipped to your color.
- If a player has no valid moves, the turn automatically passes to the opponent.
- The game ends when neither player has a valid move or when the board is completely filled.

### Ending the Game

- Upon game termination, the final board state and scores are displayed.
- The player with the highest score (most discs on the board) wins.
- In case of a tie, the game will announce the result accordingly.

## 📌 Example Gameplay

```
  0 1 2 3 4 5 6 7
0                
1                
2                
3       O X      
4       X O      
5                
6                
7                
Score - X: 2 | O: 2
Player X's turn. Valid moves: [(2, 3), (3, 2), (4, 5), (5, 4)]
Enter your move (row col): 2 3
```

## 📞 Support and Feedback

If you encounter any issues or have suggestions for improvements, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com). We appreciate your feedback and strive to continuously enhance your gaming experience.

Enjoy playing Reversi (Othello) and thank you for choosing ChatDev!
```