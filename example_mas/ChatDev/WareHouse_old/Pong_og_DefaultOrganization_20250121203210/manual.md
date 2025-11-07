# Pong Game User Manual

Welcome to the Pong Game! This manual will guide you through the installation, setup, and gameplay of our two-player Pong game developed using Python and Pygame.

## Overview

The Pong Game is a classic two-player arcade game where each player controls a vertical paddle. The objective is to bounce a ball back and forth, scoring points when the opponent misses the ball. The game is designed to be simple yet challenging, providing endless fun for players.

## Main Features

- **Two-Player Mode**: Play against a friend in a competitive match.
- **Realistic Physics**: The ball bounces off paddles and walls, simulating real-world physics.
- **Score Tracking**: Keep track of each player's score throughout the game.
- **Increasing Difficulty**: The ball speed increases with each round, adding to the challenge.

## Installation

To play the Pong Game, you need to have Python and Pygame installed on your system. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. To install Pygame, open your terminal or command prompt and run the following command:

```bash
pip install pygame==2.1.2
```

Alternatively, you can use a `requirements.txt` file to install dependencies:

```bash
pip install -r requirements.txt
```

## How to Play

### Starting the Game

1. **Run the Game**: Navigate to the directory containing the game files and execute the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Game Window**: A new window will open displaying the Pong game.

### Controls

- **Player 1**: Use the `W` key to move the left paddle up and the `S` key to move it down.
- **Player 2**: Use the `UP ARROW` key to move the right paddle up and the `DOWN ARROW` key to move it down.

### Objective

- **Score Points**: Bounce the ball past your opponent's paddle to score a point.
- **Win the Game**: The player with the most points at the end of the game wins.

### Game Mechanics

- **Ball Movement**: The ball will bounce off the top and bottom edges of the screen and the paddles.
- **Speed Increase**: The ball's speed increases with each round, making the game progressively harder.

## Troubleshooting

- **Game Not Starting**: Ensure Python and Pygame are correctly installed. Check for any error messages in the terminal.
- **Controls Not Responding**: Make sure the game window is active and in focus.

## Conclusion

Enjoy playing the Pong Game with your friends and challenge each other to see who can score the most points. We hope you have a great time!

For any further assistance or feedback, please contact our support team. Happy gaming!