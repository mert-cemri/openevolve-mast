# Pong Game User Manual

Welcome to the Pong Game! This manual will guide you through the installation, setup, and gameplay of the classic two-player Pong game developed using Python and Pygame.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Pong Game is a classic arcade game where two players control vertical paddles to bounce a ball back and forth. The objective is to score points by making the opponent miss the ball. This game is developed using Python and the Pygame library.

## Features

- Two-player mode with individual paddle controls.
- Real-time ball movement and collision detection.
- Scoring system to track player points.
- Simple and intuitive graphics.

## Installation

To run the Pong Game, you need to have Python and Pygame installed on your system. Follow the steps below to set up the environment:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. You can install it using pip:

```bash
pip install pygame
```

### Step 3: Download the Game Files

Download the game files from the repository or source provided. Ensure you have the following files:

- `main.py`
- `game.py`
- `paddle.py`
- `ball.py`
- `score.py`

### Step 4: Run the Game

Navigate to the directory containing the game files and run the following command:

```bash
python main.py
```

## How to Play

- **Player 1 Controls:** Use the `W` key to move the left paddle up and the `S` key to move it down.
- **Player 2 Controls:** Use the `UP` arrow key to move the right paddle up and the `DOWN` arrow key to move it down.
- The ball will start moving automatically. Use the paddles to bounce the ball back to the opponent.
- A player scores a point when the opponent misses the ball.
- The score is displayed at the top of the screen.

## Troubleshooting

- **Pygame Installation Issues:** Ensure you have the latest version of pip and Python. Try upgrading pip using `pip install --upgrade pip` and then reinstall Pygame.
- **Game Not Starting:** Check if all game files are in the same directory and that you are running the `main.py` file.
- **Controls Not Responding:** Ensure the game window is active and in focus when using the keyboard controls.

Enjoy playing the Pong Game! If you encounter any issues or have suggestions for improvements, feel free to reach out to the development team.