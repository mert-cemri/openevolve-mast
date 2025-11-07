```markdown
# Flappy Bird Clone

Welcome to the Flappy Bird Clone, a simple yet addictive game where you control a bird trying to fly through a series of pipes without crashing. This user manual will guide you through the installation process, introduce the main functions of the game, and explain how to play.

## Quick Install

To get started with the Flappy Bird Clone, you need to install the required dependencies. This game is built using Python and the Pygame library.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Pygame

Once Python is installed, you can install Pygame using pip. Open your terminal or command prompt and run the following command:

```bash
pip install pygame==2.1.2
```

This will install the version of Pygame required to run the game.

## Main Functions of the Software

The Flappy Bird Clone consists of several main components:

- **Bird**: The player's character, a bird that flaps to stay airborne. The player controls the bird by pressing the spacebar to flap.
- **Pipes**: Obstacles that the bird must navigate through. They appear at random intervals with varying gaps.
- **Score**: Tracks the number of pipes successfully passed by the bird. The score increases with each pipe passed.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files in your terminal or command prompt and executing:

   ```bash
   python main.py
   ```

2. **Game Controls**: 
   - Press the **Spacebar** to make the bird flap its wings and fly upwards.
   - The bird will fall due to gravity when not flapping.

3. **Objective**: 
   - Navigate the bird through the gaps in the pipes.
   - Avoid colliding with the pipes or the ground.

4. **Scoring**: 
   - Each time the bird successfully passes through a pair of pipes, the score increases by one.
   - The current score is displayed at the top-left corner of the screen.

5. **Game Over**: 
   - The game ends if the bird collides with a pipe or the ground.
   - You can restart the game by running the `main.py` file again.

## Additional Information

- **Graphics**: The game features simple 2D graphics with a sky-blue background, a yellow bird, and green pipes.
- **Performance**: The game runs at 60 frames per second for smooth gameplay.

Enjoy playing the Flappy Bird Clone and challenge yourself to achieve the highest score possible!
```
