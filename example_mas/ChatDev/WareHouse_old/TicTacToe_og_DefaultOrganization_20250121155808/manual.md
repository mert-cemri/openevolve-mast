# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user-friendly application allows two players to engage in a classic game of Tic-Tac-Toe with a graphical interface. Below, you will find detailed instructions on how to install, set up, and play the game.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Features](#game-features)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Tic-Tac-Toe Game is a simple yet engaging application designed for two players. It features a graphical user interface (GUI) built using Python's Tkinter library. Players take turns marking spaces in a 3x3 grid, aiming to align three of their marks in a row, column, or diagonal to win the game.

## Installation

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Setting Up the Environment

1. **Clone the Repository:**
   - Clone the project repository to your local machine using Git or download the source code as a ZIP file and extract it.

2. **Navigate to the Project Directory:**
   - Open a terminal or command prompt and navigate to the directory where the project files are located.

3. **Install Dependencies:**
   - Install the required dependencies by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

## How to Play

1. **Start the Game:**
   - Run the `main.py` file to launch the game. You can do this by executing the following command in your terminal or command prompt:
     ```bash
     python main.py
     ```

2. **Game Interface:**
   - A window will appear with a 3x3 grid representing the Tic-Tac-Toe board.

3. **Taking Turns:**
   - Player X starts the game. Click on any empty cell in the grid to place your mark (X or O).
   - Players alternate turns, with Player O following Player X.

4. **Winning the Game:**
   - The first player to align three of their marks in a row, column, or diagonal wins the game.
   - A message box will appear announcing the winner.

5. **Draw:**
   - If all cells are filled and no player has aligned three marks, the game ends in a draw. A message box will notify you of the draw.

6. **Restarting the Game:**
   - After a win or draw, the game automatically resets, allowing you to play again.

## Game Features

- **User-Friendly Interface:** The game features a simple and intuitive GUI, making it easy for players of all ages to enjoy.
- **Automatic Win Detection:** The game automatically detects and announces the winner or a draw.
- **Reset Functionality:** The board resets after each game, allowing for continuous play.

## Troubleshooting

- **No Display Found Error:**
  - If you encounter an error stating "No display found," ensure you are running the game on a system with a graphical display environment.

- **Python Version Compatibility:**
  - Ensure you have Python 3.6 or higher installed. You can check your Python version by running `python --version` in your terminal or command prompt.

For further assistance, please contact our support team.

Enjoy playing Tic-Tac-Toe!