```markdown
# Reversi (Othello) Game

Welcome to the Reversi (Othello) game! This software allows you to play the classic board game Reversi, where two players take turns placing discs on an 8x8 grid. The objective is to have the majority of your color discs on the board at the end of the game.

## Main Functions

- **Game Initialization**: The game starts with an initial setup of four discs in the center of the board.
- **Player Turns**: Players alternate turns, placing discs on the board.
- **Disc Flipping**: When a player places a disc, any of the opponent's discs that are in a straight line and bounded by the newly placed disc and another disc of the same color are flipped.
- **Game Over**: The game ends when the board is full or when neither player can make a valid move. The player with the most discs of their color on the board wins.

## Quick Install

To run the Reversi game, you need to have Python installed on your system. Additionally, the game requires the `pygame` library for rendering the game board and handling user interactions.

### Step 1: Install Python

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install the `pygame` library version 2.1.2, which is necessary for running the game.

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. You can do this by navigating to the directory containing the script and executing:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying an 8x8 grid. The initial setup will have two black and two white discs in the center.

3. **Making a Move**: Click on an empty square to place your disc. The game will automatically flip any opponent's discs that are captured by your move.

4. **Switching Turns**: After a valid move, the turn switches to the other player. The current player is indicated by the color of the disc you are placing.

5. **Ending the Game**: The game ends when the board is full or when no valid moves are available for either player. The winner is the player with the most discs of their color on the board.

6. **Game Over**: A message will display the winner or if the game is a draw.

Enjoy playing Reversi and strategize to outsmart your opponent!

## Documentation

For further information on the game rules and strategies, you can refer to various online resources about Reversi (Othello). This manual provides the basic instructions to get you started with the game.

Happy gaming!
```