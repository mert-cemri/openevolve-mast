# Monopoly Go! User Manual

Welcome to the simplified version of Monopoly Go! This application is a basic simulation of the classic board game Monopoly, where players roll dice, move around the board, buy properties, collect rent, and handle chance events. This manual will guide you through the installation, setup, and gameplay.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Game Setup](#game-setup)
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Troubleshooting](#troubleshooting)

## Introduction

Monopoly Go! is a simplified digital version of the classic board game Monopoly. It includes essential mechanics such as:
- Rolling dice and moving around the board
- Buying properties and collecting rent
- Handling chance events
- Tracking player money and property ownership

## Installation

### Prerequisites

To run Monopoly Go!, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository:**
   Clone the Monopoly Go! repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the name of the cloned directory.

3. **Install Dependencies:**
   This project does not require any external dependencies, so you can skip this step. Ensure you have Python installed.

## Game Setup

1. **Run the Game:**
   To start the game, execute the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Game Initialization:**
   The game initializes with two players, each starting with $1500. The board consists of properties and chance spaces.

## How to Play

1. **Player Turns:**
   - Each player takes turns rolling a dice to move around the board.
   - The player moves forward by the number of spaces rolled on the dice.

2. **Landing on Spaces:**
   - If a player lands on an unowned property, they have the option to buy it.
   - If a player lands on a property owned by another player, they must pay rent.
   - If a player lands on a chance space, they draw a chance card and follow its instructions.

3. **Winning the Game:**
   - The game continues until only one player remains with money. The last player standing is declared the winner.

## Game Features

- **Dice Rolling:** Simulates rolling a six-sided dice.
- **Property Management:** Players can buy properties and collect rent from opponents.
- **Chance Events:** Random chance cards introduce unexpected events that can benefit or hinder players.
- **Player Tracking:** Keeps track of player money, properties, and positions on the board.

## Troubleshooting

- **Python Errors:** Ensure you have Python installed and that you are running the game in the correct directory.
- **Game Crashes:** If the game crashes, restart it by running `python main.py` again.

For further assistance, please contact our support team.

Enjoy playing Monopoly Go! and may the best strategist win!