# Snake Game User Manual

Welcome to the Snake Game! This classic game allows you to control a snake as it navigates a board, eating food to grow longer while avoiding collisions with itself and the board's boundaries. This guide will help you get started with installing and playing the game.

## Main Functions of the Software

- **Snake Movement**: Control the snake using directional inputs (up, down, left, right) to move around the board.
- **Food Consumption**: The snake grows longer each time it eats a food item.
- **Game Over Conditions**: The game ends if the snake collides with itself or the boundary of the board.
- **Board Updates**: The board updates after each move, displaying the snake's current position and the location of the food.

## Quick Install

### Environment Dependencies

To run the Snake Game, you need to have Python installed on your system. Additionally, you may need to install the `curses` library, especially if you are running the game on Windows.

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Use the following command to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Note: If you are running the game on Windows, you may need to install the `windows-curses` package:

   ```bash
   pip install windows-curses
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Control the Snake**: Use the arrow keys on your keyboard to control the direction of the snake:
   - **Up Arrow**: Move the snake up.
   - **Down Arrow**: Move the snake down.
   - **Left Arrow**: Move the snake left.
   - **Right Arrow**: Move the snake right.

3. **Objective**: Navigate the snake to eat the food (represented by 'F' on the board). Each time the snake eats, it grows longer.

4. **Avoid Collisions**: The game ends if the snake collides with itself or the walls of the board.

5. **Game Over**: If the game ends, you can restart it by running the `main.py` file again.

## Troubleshooting

- **Curses Error**: If you encounter an error related to `curses`, ensure that you are using a terminal that supports `curses`. On Windows, make sure the `windows-curses` package is installed.

- **Performance Issues**: If the game runs slowly, try closing other applications to free up system resources.

Enjoy playing the classic Snake Game! If you have any questions or need further assistance, feel free to reach out to our support team.