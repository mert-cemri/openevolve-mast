# Blackjack Game User Manual

Welcome to the Blackjack Game! This manual will guide you through the installation, setup, and usage of the game. Enjoy playing Blackjack with standard rules and test your skills against the dealer.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Features](#game-features)
5. [Troubleshooting](#troubleshooting)

## Introduction

The Blackjack Game is a Python-based application that allows you to play the classic card game Blackjack. The game follows standard rules where the dealer hits up to 16 and stands on 17 or above. You can choose to 'hit,' 'stand,' or 'double down' when appropriate. The game tracks totals, detects busts, and determines the winner after each round.

## Installation

To install and run the Blackjack Game, follow these steps:

1. **Ensure Python is Installed**: Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Game Directory**: Change your directory to the game folder:
   ```bash
   cd <repository-folder>
   ```

4. **Install Dependencies**: The game requires no external dependencies beyond Python's standard library. Ensure your environment is set up correctly.

## How to Play

1. **Start the Game**: Run the main module to start the game:
   ```bash
   python main.py
   ```

2. **Place Your Bet**: Enter your bet amount when prompted. Ensure you have sufficient balance to place the bet.

3. **Player Actions**: Choose your action:
   - **Hit**: Draw another card.
   - **Stand**: Keep your current hand.
   - **Double Down**: Double your bet and draw one more card.

4. **Dealer's Turn**: The dealer will play according to the rules (hits up to 16 and stands on 17 or above).

5. **Determine Winner**: The game will automatically determine the winner and update your balance accordingly.

6. **Play Again**: After each round, you can choose to play another round or exit the game.

## Game Features

- **Standard Blackjack Rules**: Play with the classic rules of Blackjack.
- **Player Balance Management**: Start with a balance of 1000 and manage your bets.
- **Interactive Gameplay**: Make strategic decisions with 'hit,' 'stand,' and 'double down' options.
- **Automatic Winner Determination**: The game calculates and announces the winner after each round.

## Troubleshooting

- **Insufficient Balance**: Ensure you have enough balance to place your bet or double down.
- **Invalid Input**: Enter valid actions ('hit', 'stand', 'double down') when prompted.
- **Python Errors**: Ensure Python is correctly installed and the game files are intact.

Enjoy playing the Blackjack Game and may the odds be in your favor! If you encounter any issues or have questions, feel free to reach out for support.