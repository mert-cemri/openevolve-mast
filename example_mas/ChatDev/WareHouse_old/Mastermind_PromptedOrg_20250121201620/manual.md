# Mastermind Game User Manual

Welcome to the Mastermind Game! This classic code-breaking game challenges you to guess a hidden sequence of colors within a set number of tries. This manual will guide you through the installation, setup, and gameplay process.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Setup](#game-setup)
4. [How to Play](#how-to-play)
5. [Feedback System](#feedback-system)
6. [Troubleshooting](#troubleshooting)

## Introduction

The Mastermind Game is a fun and challenging puzzle where the computer selects a hidden sequence of colors, and you, the player, must guess the sequence within a limited number of attempts. After each guess, you receive feedback on how many colors are correct and in the correct position.

## Installation

To play the Mastermind Game, you need to have Python installed on your system. Follow these steps to set up the game environment:

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Game Directory**: Change your directory to the game folder:
   ```bash
   cd mastermind-game
   ```

4. **Install Dependencies**: Install any necessary dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: If there is no `requirements.txt` file, it means there are no additional dependencies required.)*

## Game Setup

The game is set up with the following default parameters:
- **Sequence Length**: 4 colors
- **Maximum Tries**: 10 attempts

These parameters can be adjusted in the `main.py` file if you wish to customize your game experience.

## How to Play

1. **Start the Game**: Run the game by executing the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Game Instructions**: Upon starting, you will receive instructions on how to play. The game will prompt you to guess the sequence of colors.

3. **Enter Your Guess**: Input your guess as a sequence of colors separated by spaces. For example:
   ```
   red blue green yellow
   ```

4. **Receive Feedback**: After each guess, you will receive feedback indicating:
   - How many colors are in the correct position.
   - How many colors are correct but in the wrong position.

5. **Win or Lose**: If you guess the sequence correctly within the allowed attempts, you win! Otherwise, the game will reveal the correct sequence after your attempts are exhausted.

## Feedback System

The feedback system provides two key pieces of information:
- **Correct Position**: The number of colors that are both correct and in the correct position.
- **Correct Color**: The number of colors that are correct but in the wrong position.

Use this feedback to refine your guesses and crack the code!

## Troubleshooting

- **Invalid Input**: Ensure your guesses match the sequence length and use valid colors. The valid colors are: red, blue, green, yellow, orange, and purple.
- **Python Errors**: Ensure Python is correctly installed and that you are running the game in the correct directory.

Enjoy the challenge and have fun playing the Mastermind Game! If you encounter any issues or have suggestions, feel free to reach out to our support team.