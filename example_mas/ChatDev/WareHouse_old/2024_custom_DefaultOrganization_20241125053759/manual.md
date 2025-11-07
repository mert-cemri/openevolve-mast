# 2048 Game User Manual

Welcome to the 2048 Game! This manual will guide you through the installation, setup, and gameplay of the 2048 game with a 10x10 grid. This game is a simple yet addictive puzzle game where the objective is to combine tiles with the same numbers to reach the highest possible score.

## Main Functions

The 2048 Game includes the following main functions:

- **Grid Management**: The game features a 10x10 grid where tiles with numbers appear. You can slide these tiles in four directions: up, down, left, and right.
- **Tile Merging**: When two tiles with the same number collide, they merge into a single tile with the sum of their values.
- **Score Tracking**: The game keeps track of your score, which increases every time tiles merge.
- **Game Over Detection**: The game ends when there are no possible moves left.

## Quick Install

To get started with the 2048 Game, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use `pip` to install the necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pygame` library, which is used for the graphical user interface.

## How to Play

1. **Start the Game**: Run the main script to start the game.
   ```bash
   python main.py
   ```

2. **Game Controls**: Use the arrow keys on your keyboard to move the tiles:
   - **Up Arrow**: Slide tiles up.
   - **Down Arrow**: Slide tiles down.
   - **Left Arrow**: Slide tiles left.
   - **Right Arrow**: Slide tiles right.

3. **Objective**: Combine tiles with the same numbers to create larger numbers and increase your score. The game ends when there are no more possible moves.

4. **Game Over**: When the game is over, a "Game Over!" message will be displayed in the console.

## Additional Information

- **Game Interface**: The game uses a simple graphical interface where tiles are displayed on a 10x10 grid. Each tile shows its current value, and the grid updates dynamically as you play.
- **Scoring**: Your score is displayed in the console and increases each time you successfully merge tiles.

Enjoy playing the 2048 Game and challenge yourself to reach the highest score possible! If you encounter any issues or have questions, please refer to the documentation or contact support for assistance.