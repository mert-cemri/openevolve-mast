```markdown
# Space Invaders Game

A simplified version of the classic Space Invaders game where the player controls a ship at the bottom of the screen, moving horizontally and firing shots to destroy descending alien rows. The game ends if aliens reach the bottom or the player defeats all aliens.

## Quick Install

To get started with the Space Invaders game, you need to install the required dependencies. This game is built using Python and the Pygame library.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

To install Pygame, run the following command in your terminal or command prompt:

```bash
pip install pygame>=2.0.0
```

Alternatively, you can install the dependencies listed in the `requirements.txt` file using:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

This is a simple, yet engaging game where you control a ship to shoot down aliens. The game provides a nostalgic experience with a modern touch, allowing players to enjoy the classic arcade feel.

### Main Features

- **Player Ship Control**: Move the ship left and right using the arrow keys and fire shots using the spacebar.
- **Alien Fleet**: Aliens descend from the top of the screen. Destroy them before they reach the bottom.
- **Game Over Conditions**: The game ends if the aliens reach the bottom of the screen or if you destroy all aliens.

## 📖 How to Play

1. **Start the Game**: Run the `main.py` file to start the game.
   ```bash
   python main.py
   ```

2. **Controls**:
   - Use the **Right Arrow Key** to move the ship to the right.
   - Use the **Left Arrow Key** to move the ship to the left.
   - Press the **Spacebar** to fire shots at the aliens.

3. **Objective**: Shoot all the aliens before they reach the bottom of the screen. If they reach the bottom, the game ends. If you destroy all aliens, you win!

4. **Game Over**: The game will display a message and close automatically if you win or if the aliens reach the bottom.

## 📖 Documentation

For further details on the game mechanics and code structure:

- **Game Initialization**: The game initializes with a ship, a fleet of aliens, and the ability to fire shots.
- **Game Loop**: The main game loop handles events, updates game objects, and refreshes the screen.
- **Collision Detection**: The game checks for collisions between shots and aliens, and between aliens and the player's ship.

Enjoy the game and have fun shooting down those aliens!
```
