# Tic-Tac-Toe Game User Manual

Welcome to the Tic-Tac-Toe Game! This user-friendly application allows two players to enjoy a classic game of Tic-Tac-Toe with an intuitive interface. Below, you'll find detailed instructions on how to install, set up, and play the game.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Main Features](#main-features)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Tic-Tac-Toe Game is a simple yet engaging application developed in Python. It allows two players to take turns marking spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Installation

To run the Tic-Tac-Toe Game, you need to have Python installed on your system. Follow these steps to set up the environment and dependencies:

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

### Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd tic-tac-toe-game
   ```

3. **Install Dependencies:**

   Ensure that you have Tkinter installed. It is typically included with Python, but if not, you can install it using your package manager. For example, on Ubuntu, you can use:

   ```bash
   sudo apt-get install python3-tk
   ```

   On macOS, Tkinter is included with Python installations from python.org.

## How to Play

1. **Start the Game:**

   Run the main script to start the game:

   ```bash
   python main.py
   ```

2. **Game Interface:**

   - A window will open displaying a 3x3 grid.
   - Player X and Player O take turns clicking on the grid to place their respective symbols.

3. **Winning the Game:**

   - The first player to align three of their symbols horizontally, vertically, or diagonally wins.
   - If all nine squares are filled without a winner, the game ends in a draw.

4. **End of Game:**

   - A message box will display the result of the game (win or draw).
   - The game window will close after acknowledging the message.

## Main Features

- **User-Friendly Interface:** The game uses a graphical interface powered by Tkinter, making it easy to play.
- **Two-Player Mode:** Allows two players to compete against each other.
- **Automatic Winner Detection:** The game automatically detects and announces the winner or a draw.

## Troubleshooting

- **Display Issues:** If you encounter issues with the display, ensure that you have a graphical display available. For remote servers, consider using a virtual display.
- **Tkinter Errors:** If you receive errors related to Tkinter, verify that it is correctly installed on your system.

We hope you enjoy playing the Tic-Tac-Toe Game! If you have any questions or feedback, please feel free to reach out to our support team.