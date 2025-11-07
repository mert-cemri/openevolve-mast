# Puzzle Game User Manual

Welcome to the Puzzle Game, where you can challenge your mind by grouping words into categories. This manual will guide you through the installation, setup, and gameplay of the Puzzle Game application.

## Overview

The Puzzle Game is an interactive application where users must group sixteen words into four categories of four words each. The game follows the standard logic of the NYT Connections game. After each guess, the game will indicate if the chosen words form a valid group. The game ends when the user forms all four correct groups or runs out of tries.

## Features

- **Interactive Gameplay**: Engage with the game through a simple command-line interface.
- **Word Categories**: Group words into predefined categories such as Fruits, Vegetables, Animals, and Colors.
- **Feedback System**: Receive immediate feedback on your guesses.
- **Limited Attempts**: Challenge yourself to complete the game within a set number of attempts.

## Installation

To run the Puzzle Game, you need to have Python installed on your system. Follow the steps below to set up the game environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Game Directory**: Change your directory to the game folder:
   ```bash
   cd <repository-folder>
   ```

4. **Install Dependencies**: Install any necessary dependencies using pip. If there are any specific dependencies, they will be listed in a `requirements.txt` file. Use the following command:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the main Python script to start the game:
   ```bash
   python main.py
   ```

2. **Enter Your Guess**: You will be prompted to enter your guess. Type four words separated by spaces that you believe form a valid category.

3. **Receive Feedback**: After each guess, the game will inform you whether your guess was correct or not.

4. **Win or Lose**: The game ends when you successfully group all words into the correct categories or exhaust your attempts.

5. **Restart**: To play again, simply rerun the `main.py` script.

## Game Logic

- **Categories**: The words are divided into four categories: Fruits, Vegetables, Animals, and Colors.
- **Attempts**: You have a maximum of 10 attempts to find all correct groups.
- **Winning**: Successfully group all words into their respective categories to win the game.
- **Losing**: If you run out of attempts without finding all groups, the game ends.

## Support

For any issues or questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

Enjoy the Puzzle Game and challenge your word grouping skills!