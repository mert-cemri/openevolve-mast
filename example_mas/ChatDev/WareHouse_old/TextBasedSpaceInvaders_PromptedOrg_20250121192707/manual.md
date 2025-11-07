# Space Invaders Game

Welcome to the Space Invaders Game! This is a simplified version of the classic arcade game where you control a ship at the bottom of the screen, moving horizontally to fire shots and destroy descending alien rows. The game ends if the aliens reach the bottom or if you defeat all the aliens.

## Main Functions

- **Player Control**: Move your ship left or right and fire shots to destroy aliens.
- **Alien Movement**: Aliens descend towards the bottom of the screen. The game ends if they reach the bottom.
- **Shooting**: Fire shots to hit and destroy aliens. The game ends when all aliens are defeated.

## Quick Install

To run the Space Invaders game, you need to have Python installed on your system. You will also need to install the required dependencies using `pip`.

1. **Install Python**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Use the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pygame` library, which is necessary to run the game.

## How to Play

1. **Run the Game**: Execute the following command in your terminal to start the game:

   ```bash
   python main.py
   ```

2. **Game Controls**:
   - **Move Left**: Press the left arrow key to move your ship to the left.
   - **Move Right**: Press the right arrow key to move your ship to the right.
   - **Fire**: Press the spacebar to fire a shot.

3. **Objective**: Destroy all the aliens before they reach the bottom of the screen. The game ends if an alien reaches the bottom or if you destroy all the aliens.

## Additional Information

- **Game Loop**: The game runs at 60 frames per second, providing smooth gameplay.
- **Collision Detection**: Shots will destroy aliens upon collision, and the game will end if all aliens are defeated.
- **Alien Movement**: Aliens move horizontally and descend gradually. If they reach the bottom, the game ends.

Enjoy playing the Space Invaders Game and aim for the highest score by defeating all the aliens!