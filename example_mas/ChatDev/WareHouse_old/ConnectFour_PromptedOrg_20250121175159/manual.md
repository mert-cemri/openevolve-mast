# Connect Four Game

Welcome to the Connect Four Game! This software allows two players to engage in a classic game of Connect Four, where the objective is to form a horizontal, vertical, or diagonal line of four discs on a seven-column, six-row grid.

## Main Functions

- **Game Initialization**: Start a new game session with a fresh board and two players.
- **Player Turns**: Players alternate turns to place their discs in the columns of the grid.
- **Win Condition**: The game checks for a win condition after each move, determining if a player has formed a line of four discs.
- **Draw Condition**: The game also checks if the board is full, resulting in a draw if no player has won.
- **User Interaction**: Players input their column choice via the console, and the board updates accordingly.

## Quick Install

This game does not require any external dependencies. However, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## How to Play

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd connect-four-game
   ```

2. **Run the Game**: Execute the main script to start the game.

   ```bash
   python main.py
   ```

3. **Gameplay Instructions**:
   - The game will display the current state of the board.
   - Players will be prompted to choose a column (0-6) to place their disc.
   - The game will check for a win or draw condition after each move.
   - The game ends when a player wins or the board is full, resulting in a draw.

4. **Player Input**: During each turn, the player will be asked to input a column number. Ensure the input is a valid number between 0 and 6. If the column is full, you will be prompted to choose another column.

5. **Winning the Game**: The first player to align four of their discs in a row, column, or diagonal wins the game.

## Additional Information

- **Game Flow**: The game alternates between two players, represented by symbols "X" and "O".
- **Board Display**: The board is displayed after each move, showing the current state of the game.
- **Error Handling**: The game handles invalid inputs and full columns gracefully, prompting the player to try again.

Enjoy playing Connect Four and may the best player win!