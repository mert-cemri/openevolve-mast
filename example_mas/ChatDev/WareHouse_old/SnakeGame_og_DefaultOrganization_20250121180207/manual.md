```markdown
# Snake Game

A classic Snake game where the player controls a snake using directional inputs to move around the board and eat 'food' items. Each time the snake eats, it grows in length. The game ends if the snake collides with itself or the boundary. The board updates after each move.

## Main Functions

- **Snake Movement**: Control the snake using the arrow keys (Up, Down, Left, Right) to navigate the board.
- **Food Consumption**: The snake grows in length each time it eats food.
- **Game Over Conditions**: The game ends if the snake collides with itself or the boundary of the board.
- **Dynamic Board Update**: The board updates after each move, reflecting the snake's new position and any changes in length.

## Installation

### Environment Setup

To run the Snake game, you need to have Python installed on your machine. Additionally, the game requires the `pygame` library for rendering graphics and handling game events.

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Install Pygame**: Use the following command to install the required version of `pygame`:

   ```bash
   pip install pygame==2.1.2
   ```

### Running the Game

1. **Clone the Repository**: Download or clone the repository containing the game code to your local machine.

2. **Navigate to the Game Directory**: Open a terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command to start the game:

   ```bash
   python main.py
   ```

## How to Play

- **Start the Game**: Launch the game using the instructions above. The game window will open, displaying the snake and the board.
- **Control the Snake**: Use the arrow keys on your keyboard to control the direction of the snake.
  - **Up Arrow**: Move the snake upwards.
  - **Down Arrow**: Move the snake downwards.
  - **Left Arrow**: Move the snake to the left.
  - **Right Arrow**: Move the snake to the right.
- **Objective**: Navigate the snake to eat the red food items that appear on the board. Each time the snake eats, it grows longer.
- **Avoid Collisions**: The game ends if the snake collides with itself or the edges of the board.

## Additional Information

- **Game Speed**: The game runs at a fixed speed, with the board updating every 0.1 seconds.
- **Restarting the Game**: To restart the game after a game over, simply close the game window and run the `main.py` file again.

Enjoy playing the classic Snake game and challenge yourself to achieve the highest score possible!
```