# 2048 Game with 10x10 Grid

Welcome to the 2048 Game with a 10x10 grid! This user manual will guide you through the installation, setup, and gameplay of this Python-based application.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [How to Play](#how-to-play)
5. [Game Controls](#game-controls)
6. [Game Rules](#game-rules)

## Introduction

The 2048 Game is a popular single-player puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. This version of the game features a larger 10x10 grid, providing a unique challenge for players.

## Features

- **10x10 Grid**: A larger grid for more complex gameplay.
- **Score Tracking**: Keep track of your score as you play.
- **Random Tile Generation**: New tiles appear randomly on the grid after each move.
- **Game Over Detection**: The game automatically detects when no more moves are possible.

## Installation

To run the 2048 game, you need to have Python installed on your system. Follow these steps to set up the game environment:

1. **Clone the Repository**: Download the game code from the repository.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org/).

3. **Run the Game**: Execute the main Python script to start the game.
   ```bash
   python main.py
   ```

## How to Play

The game starts with two tiles on the grid. Your goal is to combine tiles with the same number to create a tile with the number 2048. Use the keyboard controls to slide the tiles in different directions.

## Game Controls

- **W**: Move tiles up
- **A**: Move tiles left
- **S**: Move tiles down
- **D**: Move tiles right

After each move, a new tile with a value of 2 or 4 will appear at a random empty position on the grid.

## Game Rules

1. **Combining Tiles**: When two tiles with the same number touch, they merge into one with the sum of their values.
2. **Winning the Game**: The game is won when a tile with the number 2048 appears on the grid.
3. **Game Over**: The game ends when no more moves are possible, meaning no empty spaces are left and no adjacent tiles can be combined.

Enjoy playing the 2048 Game with a 10x10 grid and challenge yourself to reach the highest score possible!