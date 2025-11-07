# 2048 Terminal Game

A simple implementation of the classic 2048 game that can be played directly from the Linux Terminal. This game is designed to be lightweight and does not require any external dependencies or graphical user interface.

## Quick Install

No installation of external libraries is required as the game is built using Python's standard library. Ensure you have Python installed on your system.

## How to Play

### Objective

The objective of the game is to slide numbered tiles on a 4x4 grid to combine them and create a tile with the number 2048.

### Controls

- **w**: Move tiles up
- **a**: Move tiles left
- **s**: Move tiles down
- **d**: Move tiles right

### Game Rules

1. Use the keyboard keys (w, a, s, d) to move the tiles in the desired direction.
2. When two tiles with the same number touch, they merge into one with the sum of their values.
3. A new tile (2 or 4) will appear on the board after each move.
4. The game ends when there are no possible moves left.

## How to Run the Game

1. **Clone the Repository**: Download the game files to your local machine.

2. **Navigate to the Game Directory**: Open your terminal and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command in your terminal:

   ```bash
   python main.py
   ```

4. **Start Playing**: Follow the on-screen instructions to play the game.

## Game Features

- **Score Tracking**: The game keeps track of your score, which increases as you merge tiles.
- **Random Tile Spawning**: After each move, a new tile (2 or 4) is spawned at a random empty position on the grid.
- **Game Over Detection**: The game automatically detects when no more moves are possible and ends the game.

## Example Gameplay

Upon starting the game, you will see a 4x4 grid with two tiles. Use the controls to move the tiles and try to reach the 2048 tile.

```
Score: 0
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
|    |   2|    |    |
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
|    |   2|    |    |
+----+----+----+----+

Enter move (w/a/s/d):
```

## Conclusion

Enjoy the challenge of reaching the 2048 tile! This terminal-based game provides a simple yet engaging experience for fans of the classic 2048 puzzle game.