# Gomoku Game User Manual

Welcome to the Gomoku Game! This manual will guide you through the installation, setup, and gameplay of the Gomoku game developed in Python. 

## Introduction

Gomoku, also known as Five in a Row, is a classic board game played on a 15x15 grid. The objective is to be the first player to get an unbroken row of five stones horizontally, vertically, or diagonally.

## Main Functions

- **Game Initialization**: The game initializes with a 15x15 board and two players, each with a unique symbol ('X' and 'O').
- **Gameplay**: Players take turns to place their symbols on the board. The game checks for a win or draw condition after each move.
- **Win Condition**: A player wins by placing five of their symbols consecutively in a row, column, or diagonal.
- **Draw Condition**: The game ends in a draw if the board is full and no player has won.

## Quick Install

To run the Gomoku game, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

1. **Clone the Repository**: Download or clone the repository containing the game files.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. The board will be displayed, and Player X will be prompted to make the first move.

2. **Enter Moves**: Players take turns entering their moves. A move consists of two integers separated by a space, representing the row and column where the player wants to place their symbol. For example:
   ```
   Player X, enter your move (row and column): 7 7
   ```

3. **Invalid Moves**: If a player enters an invalid move (e.g., out of bounds or on an occupied space), they will be prompted to try again.

4. **Winning the Game**: The game will announce the winner when a player successfully places five of their symbols in a row.

5. **Draw**: If the board is full and no player has won, the game will declare a draw.

6. **Restarting**: To play again, simply rerun the `main.py` file.

## Additional Information

- **Dependencies**: The game is implemented in Python and does not require any external libraries beyond the standard library.
- **Customization**: You can modify the board size by changing the `size` parameter in the `Game` class initialization in `main.py`.

Enjoy playing Gomoku! If you have any questions or need further assistance, please feel free to reach out.