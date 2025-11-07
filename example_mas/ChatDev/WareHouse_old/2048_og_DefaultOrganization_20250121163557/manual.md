```markdown
# 2048 Game - 10x10 Grid

Welcome to the 2048 Game with a 10x10 grid! This user manual will guide you through the installation, setup, and gameplay of this exciting version of the classic 2048 game.

## 🎮 Game Overview

The 2048 game is a single-player sliding block puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. In this version, the grid size is expanded to 10x10, offering a unique challenge and more strategic gameplay.

## 🛠️ Main Features

- **10x10 Grid**: Unlike the traditional 4x4 grid, this version offers a larger 10x10 grid for extended gameplay.
- **Smooth Animations**: Enjoy smooth animations and transitions as you slide tiles across the grid.
- **Score Tracking**: Keep track of your score as you combine tiles and aim for the highest score possible.
- **Game Over Detection**: The game will notify you when no more moves are possible.

## 🚀 Quick Install

To get started with the 2048 game, you'll need to install the necessary environment dependencies.

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Start by cloning the game repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use `pip` to install the required dependencies listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pygame` library, which is necessary for running the game.

## 🎲 How to Play

1. **Start the Game**: Run the main script to start the game.
   ```bash
   python main.py
   ```

2. **Game Controls**: Use the arrow keys on your keyboard to move the tiles in the desired direction:
   - **Left Arrow**: Move tiles left.
   - **Right Arrow**: Move tiles right.
   - **Up Arrow**: Move tiles up.
   - **Down Arrow**: Move tiles down.

3. **Objective**: Combine tiles with the same number to create larger numbered tiles. Aim to create a tile with the number 2048.

4. **Game Over**: The game ends when no more moves are possible. Try to achieve the highest score before the game ends!

## 📖 Documentation

For more detailed information on the game mechanics and code structure, please refer to the in-code comments and documentation within the `main.py`, `game.py`, and `grid.py` files.

Enjoy playing the 2048 game with a new twist on a larger grid! Challenge yourself and see how high you can score!
```