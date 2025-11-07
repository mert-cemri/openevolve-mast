# Snake Game User Manual

Welcome to the classic Snake Game! This user manual will guide you through the installation process, introduce you to the main functions of the game, and provide instructions on how to play.

## Introduction

The Snake Game is a classic arcade game where the player controls a snake to eat food items on the board. Each time the snake eats, it grows in length. The game ends if the snake collides with itself or the boundary of the board. The board updates after each move, providing a dynamic and engaging gaming experience.

## Main Functions

- **Snake Movement**: Control the snake using directional inputs (up, down, left, right) to navigate the board.
- **Food Consumption**: The snake grows in length each time it eats a food item.
- **Collision Detection**: The game ends if the snake collides with itself or the boundary.
- **Dynamic Board Update**: The board updates after each move to reflect the current state of the game.

## Installation

To play the Snake Game, you need to have Python and the Pygame library installed on your system. Follow the steps below to set up the environment:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. You can install it using pip:

```bash
pip install pygame
```

## How to Play

1. **Run the Game**: Navigate to the directory containing the game files and run the `main.py` script using the following command:

   ```bash
   python main.py
   ```

2. **Control the Snake**: Use the arrow keys on your keyboard to control the direction of the snake:
   - **Up Arrow**: Move the snake up.
   - **Down Arrow**: Move the snake down.
   - **Left Arrow**: Move the snake left.
   - **Right Arrow**: Move the snake right.

3. **Objective**: Guide the snake to eat the red food items that appear on the board. Each time the snake eats, it grows in length.

4. **Game Over**: The game ends if the snake collides with itself or the boundary of the board. A "Game Over" message will be displayed.

5. **Restart**: To play again, simply rerun the `main.py` script.

## Additional Information

- **Game Speed**: The game runs at a default speed of 10 frames per second. You can adjust the speed by modifying the `self.clock.tick(10)` line in the `main.py` file.
- **Board Size**: The default board size is 600x400 pixels with a block size of 20 pixels. You can customize these dimensions by changing the parameters in the `Game` class initialization in `main.py`.

Enjoy playing the classic Snake Game and challenge yourself to achieve the highest score possible!