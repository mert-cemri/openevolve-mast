# 2048 Game User Manual

Welcome to the 2048 Game! This manual will guide you through the installation and usage of the game, which is designed to be played directly from the Linux Terminal. The game is implemented in Python and features a simple 4x4 grid where you can combine tiles to reach the 2048 tile.

## Quick Install

To play the 2048 game, you need to have Python installed on your system. You can check if Python is installed by running:

```bash
python --version
```

If Python is not installed, you can install it using your package manager. For example, on Ubuntu, you can use:

```bash
sudo apt update
sudo apt install python3
```

Once Python is installed, you can run the game by executing the `main.py` file.

## How to Play

The 2048 game is a single-player sliding tile puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048.

### Game Controls

- **w**: Move tiles up
- **a**: Move tiles left
- **s**: Move tiles down
- **d**: Move tiles right

### Game Rules

1. Use the keyboard controls to move the tiles in the desired direction.
2. When two tiles with the same number touch, they merge into one with the sum of their values.
3. A new tile with a value of 2 or 4 will appear on the board after each move.
4. The game ends when no more moves are possible.

### Starting the Game

To start the game, navigate to the directory containing the `main.py` file and run the following command:

```bash
python main.py
```

### Playing the Game

1. After starting the game, the initial grid will be displayed with two tiles.
2. Enter your move (w/a/s/d) to slide the tiles in the desired direction.
3. The grid will update after each valid move, and a new tile will appear.
4. Continue playing until no more moves are possible.
5. Your score will be displayed at the end of the game.

### Example Gameplay

```
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
|    |   2|    |    |
+----+----+----+----+
|    |    |    |    |
+----+----+----+----+
|    |    |    |   2|
+----+----+----+----+
Score: 0

Enter move (w/a/s/d): 
```

## Conclusion

Enjoy playing the 2048 game in your Linux Terminal! Challenge yourself to reach the 2048 tile and achieve the highest score possible. If you have any questions or encounter issues, feel free to reach out for support. Happy gaming!