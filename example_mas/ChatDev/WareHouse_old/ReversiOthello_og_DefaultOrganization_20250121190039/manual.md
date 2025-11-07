# Reversi (Othello) Game

Welcome to the Reversi (Othello) Game! This software allows you to play the classic board game Reversi, also known as Othello, against another player. The game is implemented using Python and Pygame, providing an interactive graphical interface.

## Main Functions

- **Game Initialization**: The game starts with the standard Reversi setup, with two black and two white discs in the center of the board.
- **Player Turns**: Two players take turns placing discs on the board. The current player is indicated by the color of the disc they place.
- **Disc Flipping**: When a player places a disc, any of the opponent's discs that are in a straight line and bounded by the player's discs are flipped to the player's color.
- **Game Over**: The game ends when the board is full or when neither player can make a valid move. The player with the most discs of their color on the board wins.

## Quick Install

To install the necessary environment dependencies, you need to have Python installed on your system. Then, you can install the required package using pip:

```bash
pip install -r requirements.txt
```

This command will install Pygame, which is necessary to run the graphical interface of the game.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the file in your terminal or command prompt and executing:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying an 8x8 grid representing the Reversi board. The initial setup will have two black and two white discs in the center.

3. **Making a Move**: Click on an empty square on the board to place a disc of your color. The game will automatically flip any of the opponent's discs that are flanked by your discs.

4. **Switching Turns**: After you make a move, the turn switches to the other player. The current player is indicated by the color of the disc they are placing.

5. **Ending the Game**: The game ends when the board is full or when no valid moves are available for either player. A message will be displayed indicating that the game is over.

6. **Winning the Game**: The player with the most discs of their color on the board at the end of the game is the winner.

## Additional Information

- **Game Rules**: The game follows the standard rules of Reversi. Players must place discs in such a way that they flank one or more of the opponent's discs, causing them to be flipped.
- **Valid Moves**: The game will only allow valid moves. If you attempt to place a disc in an invalid position, nothing will happen.
- **Graphical Representation**: The board is displayed using Pygame, with green squares representing the board and black and white circles representing the discs.

Enjoy playing Reversi and may the best strategist win!