# Tetris Game User Manual

Welcome to the Tetris Game developed by ChatDev! This manual will guide you through the installation, setup, and gameplay of our Tetris application. Enjoy the classic game of Tetris with a modern twist, implemented in Python.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Gameplay Instructions](#gameplay-instructions)
4. [Main Features](#main-features)
5. [Troubleshooting](#troubleshooting)

## Introduction

Tetris is a classic puzzle game where the objective is to manipulate falling tetrominoes to create complete horizontal lines, which are then cleared from the board. The game continues until no more pieces can be placed. Our version of Tetris is implemented in Python and uses the `curses` library for rendering in the terminal.

## Installation

To run the Tetris game, you need to have Python installed on your system. Follow these steps to set up the environment and dependencies:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install `curses` library**: The game uses the `curses` library for terminal rendering. This library is typically included with Python on Unix-based systems. For Windows, you may need to install a compatible version like `windows-curses`:
   ```bash
   pip install windows-curses
   ```

3. **Download the Game Code**: Clone or download the repository containing the game code.

4. **Run the Game**: Navigate to the directory containing the game files and execute the following command in your terminal:
   ```bash
   python main.py
   ```

## Gameplay Instructions

Once the game is running, you can control the tetrominoes using your keyboard:

- **Left Arrow Key**: Move the tetromino left.
- **Right Arrow Key**: Move the tetromino right.
- **Up Arrow Key**: Rotate the tetromino.
- **Down Arrow Key**: Move the tetromino down faster.

The objective is to complete horizontal lines without gaps. Each completed line increases your score. The game ends when no more tetrominoes can be placed on the board.

## Main Features

- **Random Tetromino Generation**: Each tetromino is randomly selected from the classic Tetris shapes.
- **Line Clearing and Scoring**: Completed lines are cleared, and your score increases based on the number of lines cleared.
- **Collision Detection**: The game accurately detects collisions with the board and other tetrominoes.
- **Terminal Rendering**: The game is rendered in the terminal using the `curses` library, providing a retro gaming experience.

## Troubleshooting

- **Curses Error**: If you encounter an error related to `curses`, ensure your terminal supports it. On Windows, make sure `windows-curses` is installed.
- **Performance Issues**: If the game runs slowly, try closing other applications to free up system resources.

We hope you enjoy playing our Tetris game! If you have any questions or feedback, please feel free to reach out to our support team. Happy gaming!