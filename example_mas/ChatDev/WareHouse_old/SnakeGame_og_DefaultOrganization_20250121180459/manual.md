```markdown
# Snake Game

A classic Snake game where the player controls a snake using directional inputs to move around the board and eat 'food' items. Each time the snake eats, it grows in length. The game ends if the snake collides with itself or the boundary. The board updates after each move.

## Quick Install

To get started with the Snake game, you need to install the required dependencies. The game is built using Python and the Pygame library.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Pygame

You can install the required version of Pygame using pip. Open your terminal or command prompt and run the following command:

```bash
pip install pygame==2.1.2
```

Alternatively, you can use the `requirements.txt` file to install dependencies:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The Snake game is a simple yet addictive game where you control a snake to eat food and grow longer. The challenge is to avoid running into the walls or the snake's own body.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing:

    ```bash
    python main.py
    ```

2. **Controls**: Use the arrow keys on your keyboard to control the direction of the snake:
   - **Up Arrow**: Move the snake up
   - **Down Arrow**: Move the snake down
   - **Left Arrow**: Move the snake left
   - **Right Arrow**: Move the snake right

3. **Objective**: Guide the snake to eat the red food items that appear on the screen. Each time the snake eats, it grows longer.

4. **Game Over**: The game ends if the snake collides with itself or the boundary of the game board.

5. **Restart**: To play again, simply run the `main.py` file once more.

## 🛠️ Main Functions

- **Snake Movement**: The snake moves continuously in the direction it is facing. You can change its direction using the arrow keys.
- **Growing**: The snake grows longer each time it eats a food item.
- **Collision Detection**: The game checks for collisions with the snake's own body and the boundaries of the game board.
- **Food Spawning**: Food items appear at random positions on the board, avoiding the snake's current position.

Enjoy the classic Snake game and challenge yourself to achieve the highest score possible!
```