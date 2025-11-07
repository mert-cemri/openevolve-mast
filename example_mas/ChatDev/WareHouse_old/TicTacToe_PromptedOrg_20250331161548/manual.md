# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user-friendly application allows two players to enjoy the classic game of Tic-Tac-Toe on a standard 3x3 grid. Players alternate turns to place their marks (X or O) on the grid, and the game concludes when a player wins or the board is full.

## Main Functions

- **Two-Player Mode**: The game supports two players who take turns to place their marks on the grid.
- **Winner Detection**: The game automatically detects when a player wins by completing a row, column, or diagonal with their marks.
- **Draw Detection**: If the board is full and no player has won, the game declares a draw.
- **Restart Functionality**: Players can restart the game at any time to play again.

## Quick Install

To run the Tic-Tac-Toe game, you need to have Python installed on your system. Additionally, the game uses the `tkinter` library for the graphical user interface. Follow the steps below to set up the environment and run the game:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies

The game requires the `tkinter` library, which is included with most Python installations. If you encounter any issues, you can install it using the following command:

```bash
sudo apt-get install python3-tk
```

For headless environments, the game also uses the `pyvirtualdisplay` library. Install it using:

```bash
pip install pyvirtualdisplay
```

### Step 3: Run the Game

1. Download the game files (`main.py`, `tictactoe_game.py`, `tictactoe_gui.py`).
2. Open a terminal or command prompt and navigate to the directory containing the game files.
3. Run the game using the following command:

```bash
python main.py
```

## How to Play

1. **Start the Game**: Launch the game by running `main.py`. A window will open displaying the 3x3 grid.
2. **Take Turns**: Players take turns clicking on the grid to place their marks (X or O).
3. **Winning the Game**: The game will automatically detect and announce the winner when a player completes a row, column, or diagonal with their marks.
4. **Draw**: If the board is full and no player has won, the game will declare a draw.
5. **Restart**: Click the "Restart" button to reset the game and play again.

Enjoy playing Tic-Tac-Toe with your friends! If you encounter any issues or have questions, feel free to reach out for support.