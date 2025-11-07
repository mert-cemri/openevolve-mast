# 2048 Game with 10x10 Grid

Welcome to the 2048 Game with a 10x10 grid! This user manual will guide you through the installation, setup, and usage of the game. Enjoy the challenge of reaching the 2048 tile on a larger grid!

## Quick Install

This game does not require any external dependencies, making the installation process straightforward. Simply clone the repository and run the game.

### Installation Steps

1. **Clone the Repository**

   Open your terminal and run the following command to clone the repository:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned repository.

3. **Run the Game**

   Execute the following command to start the game:

   ```bash
   python main.py
   ```

## Main Functions of the Software

The 2048 game is a single-player puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. Here's how the game works:

- **Grid**: The game is played on a 10x10 grid.
- **Tiles**: Each tile has a number, starting with 2 or 4.
- **Moves**: You can move tiles in four directions: up (w), down (s), left (a), and right (d).
- **Combining Tiles**: When two tiles with the same number collide while moving, they merge into a tile with the sum of their numbers.
- **Winning**: The game is won when a tile with the number 2048 appears on the board.
- **Game Over**: The game ends when no more moves are possible.

## How to Play

1. **Start the Game**

   Run the game using the command mentioned in the installation steps. The game will display the initial 10x10 grid with two random tiles.

2. **Make a Move**

   Enter one of the following keys to move the tiles:
   - `w`: Move tiles up
   - `s`: Move tiles down
   - `a`: Move tiles left
   - `d`: Move tiles right

3. **Continue Playing**

   Keep making moves to combine tiles and try to reach the 2048 tile. The game will display the grid after each move.

4. **Winning the Game**

   If you manage to create a tile with the number 2048, you win! The game will display a congratulatory message.

5. **Game Over**

   If no more moves are possible and you haven't reached the 2048 tile, the game will end, and a "Game Over" message will be displayed.

## Conclusion

Enjoy playing the 2048 game on a larger grid! Challenge yourself to reach the 2048 tile and beyond. If you have any questions or need further assistance, feel free to reach out to our support team. Happy gaming!