# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user manual will guide you through the installation and usage of the game, which is designed to be played directly from the Linux Terminal. The game allows two players to take turns and determines the winner or if the game is a draw.

## Quick Install

This game does not require any external dependencies, making it easy to set up and play. Simply ensure you have Python installed on your system.

### Step 1: Check Python Installation

Before you begin, make sure Python is installed on your system. You can check this by running the following command in your terminal:

```bash
python --version
```

If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Download the Game

Download the `main.py` file containing the game code. You can do this by cloning the repository or downloading the file directly.

### Step 3: Run the Game

Navigate to the directory where `main.py` is located and run the following command to start the game:

```bash
python main.py
```

## How to Play

1. **Game Start**: Once you run the game, a 3x3 tic-tac-toe board will be displayed in the terminal.

2. **Player Turns**: The game is designed for two players. Player X will start the game, followed by Player O. Players will take turns to make their moves.

3. **Making a Move**: When prompted, enter a number between 1 and 9 to place your mark (X or O) on the board. The numbers correspond to the board positions as follows:

   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

4. **Winning the Game**: The game checks for a winner after each move. A player wins by placing three of their marks in a horizontal, vertical, or diagonal row.

5. **Draw**: If all cells are filled and no player has won, the game will declare a draw.

6. **Game End**: The game will display the final board state and announce the winner or if the game is a draw. You can then choose to restart the game by running the script again.

## Troubleshooting

- **Invalid Input**: If you enter an invalid number or a number corresponding to an already occupied cell, the game will prompt you to enter a valid move.

- **Python Errors**: Ensure that Python is correctly installed and that you are running the script in the correct directory.

Enjoy playing Tic-Tac-Toe in your terminal! If you have any questions or encounter issues, please feel free to reach out for support.