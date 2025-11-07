# Monopoly Go! User Manual

Welcome to Monopoly Go!, a simplified version of the classic board game Monopoly. This game allows you to experience the thrill of property trading, rent collection, and chance events in a digital format. This manual will guide you through the installation, setup, and gameplay of Monopoly Go!.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Setup](#game-setup)
4. [How to Play](#how-to-play)
5. [Game Features](#game-features)
6. [Troubleshooting](#troubleshooting)

## Introduction

Monopoly Go! is a Python-based application that simulates a simplified version of the Monopoly board game. The game includes basic mechanics such as rolling dice, moving around the board, buying properties, collecting rent, and handling chance events. Players can track their money and property ownership throughout the game.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Basic understanding of running Python scripts.

### Quick Install

1. **Clone the Repository:**

   Clone the Monopoly Go! repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd monopoly-go
   ```

3. **Install Dependencies:**

   Although there are no external dependencies required for this project, ensure your Python environment is set up correctly.

   ```bash
   pip install -r requirements.txt
   ```

## Game Setup

1. **Run the Game:**

   Start the game by executing the `main.py` script:

   ```bash
   python main.py
   ```

2. **Graphical User Interface:**

   The game will launch with a simple graphical user interface (GUI) using Tkinter. If you encounter a warning about no display found, the game will run in a non-GUI mode.

## How to Play

1. **Starting the Game:**

   - The game begins with two players: Player 1 and Player 2.
   - Each player starts with $1500.

2. **Taking Turns:**

   - Players take turns rolling the dice by clicking the "Roll Dice" button.
   - The player moves forward on the board based on the dice roll.

3. **Buying Properties:**

   - If a player lands on an unowned property, they have the option to buy it if they have enough money.
   - The property is added to the player's list of owned properties.

4. **Paying Rent:**

   - If a player lands on a property owned by another player, they must pay rent.
   - Rent is deducted from the player's money and added to the property owner's money.

5. **Chance Events:**

   - Landing on a "Chance" space triggers a random chance event.
   - Events can include collecting money, advancing to a specific board position, etc.

## Game Features

- **Dice Rolling:** Simulates rolling a six-sided dice.
- **Property Management:** Buy properties and collect rent from opponents.
- **Chance Events:** Random events that can affect players' positions and finances.
- **Player Tracking:** Monitor each player's position, money, and property ownership.

## Troubleshooting

- **No Display Found:** If you receive a warning about no display found, ensure you have a graphical environment set up, or run the game in non-GUI mode.
- **Insufficient Funds:** If a player cannot afford rent or property purchase, consider implementing additional game rules for handling bankruptcy or skipping payments.

Enjoy playing Monopoly Go! and experience the excitement of property trading and strategic decision-making. For any further assistance, feel free to reach out to our support team.