```markdown
# Space Invaders Game

A simplified version of the classic Space Invaders game where the player controls a ship at the bottom of the screen, moving horizontally and firing shots to destroy descending alien rows. The game ends if aliens reach the bottom or the player defeats all aliens.

## Main Features

- **Player Control**: Move the player's ship left or right and shoot bullets to destroy aliens.
- **Alien Movement**: Aliens move horizontally and descend towards the player. The game ends if they reach the bottom.
- **Game Over Conditions**: The game ends when all aliens are defeated or if any alien reaches the bottom of the screen.

## Installation

To run the Space Invaders game, you need to have Python and Pygame installed on your system. Follow the steps below to set up the environment and start the game.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. You can install it using pip:

```bash
pip install pygame==2.1.2
```

### Step 3: Download the Game Code

Clone or download the game code from the repository.

### Step 4: Run the Game

Navigate to the directory containing the game code and run the main script:

```bash
python main.py
```

## How to Play

- **Movement**: Use the left and right arrow keys to move the player's ship horizontally.
- **Shooting**: Press the spacebar to shoot bullets at the aliens.
- **Objective**: Destroy all aliens before they reach the bottom of the screen.

## Game Files

- **main.py**: The main entry point for the game. Initializes and starts the game loop.
- **game.py**: Manages the game loop, handles events, and updates the game state.
- **player.py**: Represents the player's ship, handling movement and shooting.
- **alien.py**: Represents the alien enemies, managing their movement and behavior.
- **bullet.py**: Represents the bullets fired by the player.
- **game_object.py**: Base class for all game objects (Player, Alien, Bullet).

## Troubleshooting

- Ensure all dependencies are installed correctly.
- If the game does not start, check for any error messages in the console and ensure Pygame is installed.
- For further assistance, refer to the Pygame documentation or seek help from online forums.

Enjoy playing Space Invaders!
```