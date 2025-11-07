# Match-3 Puzzle Game User Manual

Welcome to the Match-3 Puzzle Game, a fun and engaging game reminiscent of the popular Candy Crush. This manual will guide you through the installation, setup, and gameplay of the application.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Setup](#game-setup)
4. [How to Play](#how-to-play)
5. [Game Features](#game-features)
6. [Troubleshooting](#troubleshooting)

## Introduction

The Match-3 Puzzle Game is a Python-based application that allows users to swap adjacent candies on a board to form matches of three or more. Matches are cleared, new candies appear, and scoring is tracked. The board updates after each valid move, providing an engaging and dynamic gameplay experience.

## Installation

To get started with the Match-3 Puzzle Game, you need to install the necessary environment dependencies. Follow the steps below:

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installing Dependencies

1. Clone the repository or download the source code to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the source code.

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pygame` library, which is necessary for running the game.

## Game Setup

Once the dependencies are installed, you can set up the game by following these steps:

1. Ensure you are in the directory containing the `main.py` file.

2. Run the game using the following command:

   ```bash
   python main.py
   ```

   This will launch the game window, and you will be ready to start playing.

## How to Play

The objective of the Match-3 Puzzle Game is to swap adjacent candies to form horizontal or vertical lines of three or more matching candies. Here's how you can play:

1. **Select a Candy:** Click on a candy to select it. The selected candy will be highlighted.

2. **Swap Candies:** Click on an adjacent candy to swap it with the selected candy. If the swap results in a match of three or more candies, the candies will be cleared, and new candies will fall into place.

3. **Score Points:** Each cleared candy adds points to your score. The score is displayed at the top of the game window.

4. **Continue Playing:** Keep making matches to increase your score. The game continues until there are no more possible moves.

## Game Features

- **Dynamic Board:** The game board updates after each valid move, providing a continuous and engaging experience.

- **Scoring System:** Track your progress with a real-time score display.

- **Randomized Candies:** Each game starts with a randomly generated board, ensuring a unique experience every time.

## Troubleshooting

If you encounter any issues while running the game, consider the following troubleshooting tips:

- **Ensure Python and Pygame are Installed:** Verify that Python and the `pygame` library are correctly installed on your system.

- **Check for Errors:** If the game does not start, check the terminal or command prompt for any error messages and resolve them accordingly.

- **Update Dependencies:** Ensure all dependencies are up to date by running `pip install -r requirements.txt` again.

We hope you enjoy playing the Match-3 Puzzle Game! If you have any further questions or need assistance, feel free to reach out to our support team. Happy gaming!