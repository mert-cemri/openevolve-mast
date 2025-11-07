# 2048 Game - 10x10 Grid

Welcome to the 2048 Game with a 10x10 grid! This game is a larger variant of the classic 2048 puzzle game, where the objective is to combine tiles with the same numbers to reach the highest possible score. This version is implemented using Python and Pygame.

## Main Functions

- **Game Initialization**: The game starts with a 10x10 grid, initially populated with two tiles, each having a value of either 2 or 4.
- **Tile Movement**: Players can move tiles in four directions: UP, DOWN, LEFT, and RIGHT. Tiles with the same value merge into one when they collide.
- **Score Tracking**: The game keeps track of the player's score, which increases as tiles are merged.
- **Game Over Detection**: The game ends when no more moves are possible.

## Quick Install

To get started with the 2048 Game, you'll need to install the required dependencies. Follow these steps to set up your environment:

1. **Clone the Repository**: First, clone the repository containing the game code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use pip to install the necessary Python packages. Make sure you have Python and pip installed on your system.

   ```bash
   pip install -r requirements.txt
   ```

   This will install Pygame, which is required to run the game.

## How to Play

1. **Run the Game**: Navigate to the directory where the game files are located and execute the main script.

   ```bash
   python main.py
   ```

2. **Game Controls**: Use the arrow keys on your keyboard to move the tiles in the desired direction:
   - **UP Arrow**: Move tiles up.
   - **DOWN Arrow**: Move tiles down.
   - **LEFT Arrow**: Move tiles left.
   - **RIGHT Arrow**: Move tiles right.

3. **Objective**: Combine tiles with the same numbers to create larger numbered tiles. Try to achieve the highest score possible before the grid fills up and no more moves are available.

4. **Game Over**: The game will display a "Game Over" message when no more moves are possible.

## Additional Information

- **Grid Size**: This version of the game uses a 10x10 grid, providing a larger playing area compared to the standard 4x4 grid.
- **Tile Values**: New tiles appear with a value of 2 or 4, with a 90% chance of being a 2.
- **Scoring**: Your score increases each time you merge tiles. The score is displayed at the top of the game window.

Enjoy playing the 2048 Game with a 10x10 grid and challenge yourself to reach the highest score possible! If you encounter any issues or have suggestions for improvements, feel free to contribute to the project or reach out to the development team.