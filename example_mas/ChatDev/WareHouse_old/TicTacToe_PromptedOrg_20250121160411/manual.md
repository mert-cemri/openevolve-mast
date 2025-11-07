# Tic-Tac-Toe Game

Welcome to the Tic-Tac-Toe game! This application allows two players to take turns playing the classic game of Tic-Tac-Toe. The game is designed with a user-friendly interface and determines the winner or if the game ends in a draw.

## Quick Install

To get started with the Tic-Tac-Toe game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the game by following these steps:

1. Clone the repository or download the source code files (`main.py`, `game.py`, `board.py`) to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the files are located.

3. Run the following command to start the game:

   ```bash
   python main.py
   ```

## 🤔 What is this?

The Tic-Tac-Toe game is a simple, yet engaging application that allows two players to compete against each other. The game board is a 3x3 grid, and players take turns placing their markers (either 'X' or 'O') on the grid. The objective is to get three of your markers in a row, column, or diagonal before your opponent does.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file to start the game. The game will prompt Player X to make the first move.

2. **Make a Move**: Players will be asked to enter the row and column numbers where they want to place their marker. The input should be a number between 1 and 3.

3. **Invalid Moves**: If a player tries to place a marker on an already occupied spot or enters an invalid number, they will be prompted to try again.

4. **Winning the Game**: The game checks for a winner after each move. A player wins by placing three of their markers in a row, column, or diagonal.

5. **Draw**: If all spots on the board are filled and no player has won, the game ends in a draw.

6. **Switch Players**: After a valid move, the game automatically switches to the other player.

7. **End of Game**: The game announces the winner or if the game is a draw, and then terminates.

## Example

Here's an example of how the game might look during play:

```
 | | 
-----
 | | 
-----
 | | 
Player X, enter the row (1, 2, or 3): 1
Player X, enter the column (1, 2, or 3): 1
X| | 
-----
 | | 
-----
 | | 
Player O, enter the row (1, 2, or 3): 2
Player O, enter the column (1, 2, or 3): 2
X| | 
-----
 |O| 
-----
 | | 
```

Continue playing until a player wins or the game ends in a draw.

Enjoy the game and have fun competing with your friends!