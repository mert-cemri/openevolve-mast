# Tic-Tac-Toe Game

Welcome to the Tic-Tac-Toe Game! This user-friendly application allows two players to take turns and determine the winner in a classic game of Tic-Tac-Toe. This manual will guide you through the installation process, main functions, and how to play the game.

## Quick Install

To run the Tic-Tac-Toe game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, follow these steps to set up the game:

1. **Clone the Repository:**
   - Clone the repository containing the game code to your local machine.

2. **Navigate to the Game Directory:**
   - Open a terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game:**
   - Execute the following command to start the game:
     ```
     python main.py
     ```

## Main Functions of the Software

The Tic-Tac-Toe game consists of two main files:

1. **main.py:**
   - This is the main file that initializes the game and handles the game loop. It prompts players for their moves, updates the game state, and checks for a winner or a draw.

2. **game.py:**
   - This file contains the `Game` class, which manages the game state and logic. It includes functions to display the board, make moves, check for a winner, determine if the game is a draw, and switch players.

## How to Play

1. **Starting the Game:**
   - Run the `main.py` file to start the game. The game will display an empty Tic-Tac-Toe board.

2. **Taking Turns:**
   - Players take turns to enter their moves. The current player is prompted to enter their move in the format 'row column' (e.g., '1 2').

3. **Making a Move:**
   - Enter the row and column numbers (0, 1, or 2) to place your mark ('X' or 'O') on the board. The board is a 3x3 grid, and the top-left corner is (0, 0).

4. **Checking for a Winner:**
   - After each move, the game checks for a winner. If a player has three of their marks in a row, column, or diagonal, they win the game.

5. **Draw Condition:**
   - If all cells are filled and no player has won, the game is declared a draw.

6. **Switching Players:**
   - After a valid move, the game switches to the other player.

7. **Ending the Game:**
   - The game ends when a player wins or the game is a draw. You can restart the game by running `main.py` again.

Enjoy playing the Tic-Tac-Toe game and may the best player win! If you encounter any issues or have questions, feel free to reach out for support.