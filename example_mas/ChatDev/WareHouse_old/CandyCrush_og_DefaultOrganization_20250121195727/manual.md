# Match-3 Puzzle Game User Manual

Welcome to the Match-3 Puzzle Game, a captivating and engaging game reminiscent of Candy Crush. This manual will guide you through the installation process, introduce the main functions of the game, and provide instructions on how to play.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Overview](#game-overview)
4. [How to Play](#how-to-play)
5. [Scoring](#scoring)
6. [Troubleshooting](#troubleshooting)

## Introduction

The Match-3 Puzzle Game is a fun and addictive game where players swap adjacent candies to form matches of three or more. Matches are cleared, new candies appear, and the player's score is tracked. The game board updates after each valid move, providing endless entertainment.

## Installation

To play the Match-3 Puzzle Game, you need to have Python and the Pygame library installed on your system. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Once Python is installed, open your terminal or command prompt and run the following command to install Pygame:

```bash
pip install pygame>=2.0.0
```

### Step 3: Download the Game Files

Download the game files, including `main.py`, `board.py`, `candy.py`, and `score.py`, and place them in the same directory.

## Game Overview

The Match-3 Puzzle Game consists of the following components:

- **Game Board**: An 8x8 grid filled with colorful candies.
- **Candies**: Different types of candies represented by various colors.
- **Score**: A score tracker that updates based on the number of matches cleared.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing the following command:

   ```bash
   python main.py
   ```

2. **Swap Candies**: Click on a candy and then click on an adjacent candy to swap their positions. The goal is to form a horizontal or vertical line of three or more candies of the same type.

3. **Clear Matches**: When a match is formed, the candies will disappear, and new candies will drop from the top to fill the empty spaces.

4. **Continue Playing**: Keep swapping candies to form matches and increase your score. The game continues until you decide to quit.

## Scoring

- Each candy cleared as part of a match adds 10 points to your score.
- The score is displayed at the top-left corner of the game screen.

## Troubleshooting

- **Game Not Starting**: Ensure Python and Pygame are correctly installed. Check for any error messages in the terminal for additional guidance.
- **Graphics Issues**: Make sure your system supports Pygame and that your graphics drivers are up to date.

Enjoy playing the Match-3 Puzzle Game! If you encounter any issues or have feedback, please contact our support team. Happy gaming!