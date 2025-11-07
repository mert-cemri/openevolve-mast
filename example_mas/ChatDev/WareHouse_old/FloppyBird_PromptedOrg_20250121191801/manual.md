# Flappy Bird Clone

Welcome to the Flappy Bird Clone, a simple yet addictive game where you control a bird trying to fly through a series of pipes without crashing. This user manual will guide you through the installation process, introduce the main functions of the software, and explain how to play the game.

## Quick Install

To run the Flappy Bird Clone, you need to have Python installed on your system. Additionally, the game requires the `pygame` library. You can install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## 🎮 What is this?

The Flappy Bird Clone is a Python-based game that mimics the popular Flappy Bird game. The objective is to keep the bird flying by pressing a key to flap its wings, avoiding obstacles in the form of pipes. The game ends when the bird collides with a pipe or the ground. Each successful pass through the pipes increases your score.

## Main Functions

- **Flap**: Press the spacebar to make the bird flap its wings and fly upwards.
- **Score**: Earn points by successfully navigating the bird through the gaps in the pipes.
- **Game Over**: The game ends if the bird hits a pipe or the ground.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Control the Bird**: Use the spacebar to make the bird flap its wings. Each press will give the bird an upward thrust.

3. **Avoid Obstacles**: Navigate the bird through the gaps in the pipes. The pipes move from right to left, and you must avoid hitting them.

4. **Scoring**: Each time the bird successfully passes through a set of pipes, your score increases by one.

5. **Game Over**: The game ends if the bird collides with a pipe or the ground. Your final score will be displayed on the screen.

## 📖 Documentation

For more detailed information on the game's code and structure, you can explore the following modules:

- **main.py**: The main module that initializes and runs the game.
- **bird.py**: Contains the `Bird` class, which represents the bird character and its behaviors.
- **pipe.py**: Contains the `Pipe` class, which represents the pipes and their movements.
- **score.py**: Handles the scoring system and displays the score on the screen.
- **constants.py**: Stores game constants such as screen dimensions, colors, and physics parameters.

Enjoy the game and try to beat your high score!