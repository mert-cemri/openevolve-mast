# Reversi (Othello) Game

Welcome to the Reversi (Othello) game, a classic strategy board game implemented in Python using the Pygame library. This user manual will guide you through the installation process, introduce the main functions of the software, and explain how to play the game.

## Quick Install

To get started with the Reversi game, you need to install the required dependencies. The game is built using Python and Pygame, so make sure you have Python installed on your system.

### Step 1: Install Python

If you haven't already, download and install Python from the official [Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Once Python is installed, you can install Pygame using pip. Open your terminal or command prompt and run the following command:

```bash
pip install pygame==2.1.2
```

This will install the specific version of Pygame required for the game.

## Main Functions of the Software

The Reversi game software consists of several key components:

- **Game Board**: An 8x8 grid where players place their discs. The board is initialized with two black and two white discs in the center.

- **Players**: Two players take turns placing discs on the board. One player uses black discs, and the other uses white discs.

- **Game Logic**: The game handles the placement of discs, checks for valid moves, flips opponent discs, and determines when the game ends.

- **Graphical Interface**: The game uses Pygame to render the board and discs, providing a visual representation of the game state.

## How to Play

### Starting the Game

1. **Run the Game**: Open your terminal or command prompt, navigate to the directory containing the game files, and run the following command:

   ```bash
   python main.py
   ```

   This will launch the game window.

2. **Game Interface**: The game window displays an 8x8 grid representing the board. The initial setup includes two black and two white discs in the center.

### Playing the Game

1. **Turn-Based Play**: Players take turns placing their discs on the board. The player with black discs goes first.

2. **Placing Discs**: Click on an empty square on the board to place your disc. The move is valid if it results in flipping at least one of the opponent's discs.

3. **Flipping Discs**: When a valid move is made, all opponent discs that lie in a straight line between the newly placed disc and another disc of the same color are flipped to the player's color.

4. **Switching Turns**: After a valid move, the turn switches to the other player. If a player has no valid moves, the turn automatically switches back.

5. **Game End**: The game ends when the board is full or neither player has a valid move. The player with the most discs on the board wins.

### Exiting the Game

To exit the game, simply close the game window or press the close button.

## Conclusion

Enjoy playing Reversi (Othello) and challenge your strategic thinking! If you encounter any issues or have questions, feel free to reach out for support. Happy gaming!