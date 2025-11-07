```markdown
# Snake Game

A classic Snake game where the player controls a snake using directional inputs to move around the board and eat 'food' items. Each time the snake eats, it grows in length. The game ends if the snake collides with itself or the boundary. The board updates after each move.

## Quick Install

To get started with the Snake Game, you need to install the necessary environment dependencies. The game is built using Python and the Pygame library.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Pygame

Install Pygame using pip, which is the package installer for Python. Open your terminal or command prompt and run the following command:

```bash
pip install pygame>=2.0.0
```

Alternatively, you can use the `requirements.txt` file to install the dependencies:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The Snake Game is a simple yet engaging game where the player maneuvers a snake to eat food and grow longer. The challenge is to avoid running into the snake's own body or the game boundaries.

### Main Features

- **Directional Control**: Use the arrow keys to control the direction of the snake.
- **Food Consumption**: The snake grows longer each time it eats food.
- **Collision Detection**: The game ends if the snake collides with itself or the boundaries.
- **Dynamic Gameplay**: The board updates after each move, providing a dynamic gaming experience.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing the following command:

    ```bash
    python main.py
    ```

2. **Control the Snake**: Use the arrow keys on your keyboard to change the direction of the snake:
   - **Up Arrow**: Move the snake up.
   - **Down Arrow**: Move the snake down.
   - **Left Arrow**: Move the snake left.
   - **Right Arrow**: Move the snake right.

3. **Objective**: Guide the snake to eat the red food squares that appear on the board. Each time the snake eats, it grows longer.

4. **Avoid Collisions**: The game ends if the snake collides with the edges of the board or with itself.

5. **Enjoy the Game**: Try to achieve the highest score possible by eating as much food as you can without colliding.

## 📖 Documentation

For further information and documentation, please refer to the source code files:

- **main.py**: Contains the main game loop and initialization.
- **snake.py**: Manages snake behavior including movement, growth, and collision detection.
- **food.py**: Manages food behavior including position randomization and rendering.
- **utils.py**: Provides utility functions for drawing the game grid.

Enjoy playing the classic Snake Game and challenge yourself to beat your high score!
```