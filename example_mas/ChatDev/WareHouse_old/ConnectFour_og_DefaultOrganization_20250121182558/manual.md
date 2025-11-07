# Connect Four Game User Manual

Welcome to the Connect Four Game! This application allows two players to enjoy the classic Connect Four game on a digital platform. Below, you will find detailed instructions on how to install, set up, and play the game.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Features](#game-features)
5. [Troubleshooting](#troubleshooting)

## Introduction

Connect Four is a two-player connection game in which the players first choose a color and then take turns dropping colored discs into a seven-column, six-row grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- No external dependencies are required for this application.

### Steps to Install

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Clone the repository using the following command:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the cloned directory:
     ```bash
     cd <repository-directory>
     ```

2. **Run the Game:**
   - Execute the main script to start the game:
     ```bash
     python main.py
     ```

## How to Play

1. **Starting the Game:**
   - Run the `main.py` script as described in the installation section.
   - A window will appear with a blue grid representing the Connect Four board.

2. **Gameplay:**
   - Player 1 starts the game and is represented by red discs.
   - Player 2 follows and is represented by yellow discs.
   - Players take turns clicking on the column where they want to drop their disc.
   - The game will automatically update the board and display whose turn it is.

3. **Winning the Game:**
   - The first player to connect four of their discs in a row, column, or diagonal wins the game.
   - A message will appear declaring the winner.

4. **Draw:**
   - If the board is completely filled and no player has connected four discs, the game ends in a draw.

## Game Features

- **Graphical User Interface:** The game features a user-friendly GUI using the Tkinter library.
- **Real-time Updates:** The board updates in real-time after each move.
- **Win/Draw Detection:** The game automatically detects and announces a win or draw.

## Troubleshooting

- **Game Does Not Start:**
  - Ensure Python is installed and added to your system's PATH.
  - Verify that you are in the correct directory where the `main.py` file is located.

- **Unexpected Behavior:**
  - Restart the game by closing the window and running the `main.py` script again.

We hope you enjoy playing Connect Four! If you encounter any issues or have suggestions for improvement, please feel free to contact us. Happy gaming!