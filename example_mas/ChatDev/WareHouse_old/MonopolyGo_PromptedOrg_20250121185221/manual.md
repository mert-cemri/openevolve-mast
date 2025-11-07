# Monopoly Go! User Manual

Welcome to Monopoly Go!, a simplified version of the classic board game Monopoly. This game allows you to experience the thrill of property trading, rent collection, and chance events in a digital format. This manual will guide you through the installation process, introduce you to the main functions of the game, and provide instructions on how to play.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Main Functions](#main-functions)
4. [How to Play](#how-to-play)
5. [Game Rules](#game-rules)

## Introduction

Monopoly Go! is a Python-based application that simulates a simplified version of Monopoly. Players take turns rolling dice, moving around the board, buying properties, collecting rent, and encountering chance events. The objective is to be the last player remaining with money.

## Installation

To play Monopoly Go!, you need to have Python installed on your system. Follow these steps to set up the game environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Download the game files from the repository.

   ```bash
   git clone https://github.com/your-repo/monopoly-go.git
   cd monopoly-go
   ```

3. **Install Dependencies**: Install any required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

   Note: If there is no `requirements.txt` file, it means there are no additional dependencies required beyond Python itself.

## Main Functions

Monopoly Go! consists of several key components:

- **Game Management**: The `Game` class in `main.py` manages the game flow, including starting the game, handling player turns, and checking for a winner.

- **Board Management**: The `Board` class in `board.py` represents the game board and manages spaces, including properties and chance cards.

- **Player Management**: The `Player` class in `player.py` represents each player, handling movement, property transactions, and chance events.

- **Property Management**: The `Property` class in `property.py` represents properties on the board, managing ownership and rent transactions.

- **Dice Rolling**: The `Dice` class in `dice.py` simulates dice rolling.

- **Chance Events**: The `Chance` class in `chance.py` handles random chance events that affect gameplay.

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game.

   ```bash
   python main.py
   ```

2. **Enter Player Names**: The game will prompt you to enter the names of the players.

3. **Take Turns**: Players take turns rolling the dice and moving around the board. The game will display relevant information and prompt players for decisions, such as buying properties or paying rent.

4. **Win the Game**: The game continues until only one player remains with money. The last player standing wins the game.

## Game Rules

- **Rolling Dice**: Players roll a six-sided die to determine how many spaces to move.

- **Buying Properties**: Players can buy unowned properties if they have enough money.

- **Paying Rent**: If a player lands on a property owned by another player, they must pay rent.

- **Chance Events**: Landing on a chance space triggers a random event that can affect a player's position or money.

- **Bankruptcy**: If a player's money falls below zero, they are removed from the game.

Enjoy playing Monopoly Go! and may the best strategist win!