```markdown
# Gomoku Game

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku, also known as Five in a Row, against another player. The game is implemented in Python and features a graphical user interface (GUI) using Tkinter.

## Main Functions

- **Game Logic**: The core logic of the Gomoku game is implemented in `gomoku.py`. It handles the game board, player turns, and win condition checks.
- **Graphical User Interface**: The GUI is implemented in `gui.py` using Tkinter. It provides a visual representation of the board and allows players to interact with the game using mouse clicks.
- **Game Management**: The application manages game states, including starting a new game and displaying the current player's turn.

## Installation

### Environment Setup

This project does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**: Download the project files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the main script to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run `main.py` to launch the game window.
2. **Game Interface**: The game board will be displayed in a window. The board consists of a 15x15 grid, which is the standard size for Gomoku.
3. **Making a Move**: Click on an empty intersection on the board to place your piece. The game alternates turns between two players: Black and White.
4. **Winning the Game**: The objective is to be the first player to form an unbroken chain of five stones horizontally, vertically, or diagonally.
5. **Game Over**: When a player wins, a message will be displayed. You can choose to start a new game by responding to the prompt.

## Additional Information

- **Current Player Indicator**: The current player is displayed at the top of the game window.
- **New Game Prompt**: After a game ends, you will be prompted to start a new game. Click 'Yes' to reset the board and begin again.

Enjoy playing Gomoku and challenge your friends to see who can master the board!

```
