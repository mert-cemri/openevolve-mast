```markdown
# Gomoku Game

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku, also known as Five in a Row, against another player. The game is implemented using Python and Pygame, providing a simple and interactive graphical interface.

## Main Functions

- **Game Board**: A 15x15 grid where players take turns placing their symbols (X or O).
- **Two Players**: The game supports two players, each taking turns to place their symbol on the board.
- **Win Detection**: The game automatically detects when a player has won by placing five of their symbols in a row, either horizontally, vertically, or diagonally.
- **Draw Detection**: The game can also detect when the board is full and the game ends in a draw.
- **Reset Functionality**: Players can reset the game to start a new match.

## Quick Install

To run the Gomoku Game, you need to have Python and Pygame installed on your system. Follow these steps to set up your environment:

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: Use pip to install Pygame, which is required for the graphical interface.
   ```bash
   pip install pygame>=2.0.0
   ```

3. **Download the Game Files**: Ensure you have all the necessary Python files (`main.py`, `game.py`, `board.py`, `player.py`) in the same directory.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Game Interface**: A window will open displaying the Gomoku board. The board consists of a 15x15 grid.

3. **Taking Turns**: Players take turns clicking on the grid to place their symbol (X for Player 1 and O for Player 2). The game automatically switches turns after each move.

4. **Winning the Game**: The first player to align five of their symbols in a row (horizontally, vertically, or diagonally) wins the game. A message will be displayed announcing the winner.

5. **Draw**: If the board is full and no player has aligned five symbols, the game ends in a draw.

6. **Resetting the Game**: Close and reopen the application to start a new game.

## Additional Information

- **Game Logic**: The game logic is handled in `game.py`, which manages player turns, move validation, and win/draw conditions.
- **Board Management**: The board state and rendering are managed in `board.py`.
- **Player Representation**: Players are represented by the `Player` class in `player.py`.

Enjoy playing Gomoku and challenge your friends to see who can master the board!
```