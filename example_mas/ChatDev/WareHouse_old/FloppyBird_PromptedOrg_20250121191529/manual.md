# Flappy Bird Clone User Manual

Welcome to the Flappy Bird Clone! This manual will guide you through the installation, setup, and gameplay of the Flappy Bird clone developed using Python and Pygame.

## Table of Contents

1. [Introduction](#introduction)
2. [Main Functions](#main-functions)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Flappy Bird Clone is a simple yet addictive game where the player controls a bird, navigating it through a series of pipes. The objective is to keep the bird flying by pressing a key to 'flap' and avoid colliding with the pipes or the ground. Each successful pass through the pipes increases the player's score.

## Main Functions

- **Bird Control**: Press the spacebar to make the bird flap and stay airborne.
- **Pipe Generation**: Pipes with randomly generated vertical gaps appear from the right side of the screen.
- **Scoring System**: Each successful pass through the pipes increases the score.
- **Game Over**: The game ends if the bird collides with a pipe or the ground.

## Installation

To run the Flappy Bird Clone, you need to have Python and Pygame installed on your system. Follow the steps below to set up the environment:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. You can install it using pip:

```bash
pip install pygame
```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Game Controls**: Use the spacebar to make the bird flap and stay in the air. The objective is to navigate the bird through the gaps in the pipes without hitting them or the ground.

3. **Scoring**: Each time the bird successfully passes through a pair of pipes, your score increases by one.

4. **Game Over**: The game ends if the bird collides with a pipe or the ground. You can restart the game by running the `main.py` file again.

## Troubleshooting

- **Pygame Installation Issues**: If you encounter issues installing Pygame, ensure that your Python environment is correctly set up and that you have the necessary permissions to install packages.

- **Game Not Starting**: If the game does not start, check for any error messages in the terminal. Ensure that all game files (`main.py`, `game.py`, `bird.py`, `pipe.py`, `score.py`) are in the same directory and that you are running the correct Python version.

- **Performance Issues**: If the game runs slowly, try closing other applications to free up system resources.

We hope you enjoy playing the Flappy Bird Clone! If you have any questions or need further assistance, please feel free to reach out to our support team.