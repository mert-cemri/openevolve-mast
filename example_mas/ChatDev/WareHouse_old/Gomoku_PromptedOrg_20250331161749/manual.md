```markdown
# Gomoku Game

Welcome to the Gomoku Game, a classic strategy board game implemented in Python. This game is played on a 15x15 board where two players alternate placing black or white stones. The objective is to form an unbroken row of five stones horizontally, vertically, or diagonally.

## Quick Install

To get started with the Gomoku Game, you need to have Python installed on your system. This game does not require any external dependencies, so you can simply clone the repository and run the game.

### Installation Steps

1. **Clone the Repository:**

   Open your terminal or command prompt and run the following command to clone the repository:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned repository folder.

3. **Run the Game:**

   Execute the following command to start the game:

   ```bash
   python main.py
   ```

## 🤔 What is this?

Gomoku is a traditional board game that challenges players to strategically place stones on a grid to form a line of five stones. This implementation allows two players to compete against each other on a 15x15 board.

## 📖 How to Play

1. **Start the Game:**

   When you run the game, the board will be displayed in the console, showing a 15x15 grid filled with dots ('.') representing empty spaces.

2. **Player Moves:**

   Players take turns to place their stones on the board. Player 'B' (Black) starts first, followed by Player 'W' (White).

   - To make a move, enter the row and column numbers separated by a space when prompted. For example, to place a stone at row 3, column 5, enter `3 5`.

3. **Winning the Game:**

   The game continues until one player forms an unbroken row of five stones horizontally, vertically, or diagonally. The game will announce the winner and end.

4. **Invalid Moves:**

   - If a player attempts to place a stone outside the board boundaries or on an already occupied cell, the game will prompt for a valid move.

5. **Game Over:**

   Once a player wins, the game will display the winning message and terminate.

## Example

Here's a quick example of how the game might look during play:

```
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .
. . . . . . . . . . . . . . .

Player B, enter your move (row and column): 7 7
```

Enjoy playing Gomoku and may the best strategist win!
```