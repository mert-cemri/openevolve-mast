# Tower of the Sorcerer - User Manual

Welcome to "Tower of the Sorcerer," a roguelike game inspired by classic dungeon crawlers. This manual will guide you through the installation, main features, and gameplay mechanics of the game.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Features](#game-features)
4. [How to Play](#how-to-play)
5. [Troubleshooting](#troubleshooting)

## Introduction

"Tower of the Sorcerer" is a roguelike game where players navigate through a dungeon filled with monsters, treasure chests, and obstacles. The objective is to reach the door to the next level while managing your health points (HP) and overcoming challenges.

## Installation

To play "Tower of the Sorcerer," you need to set up your environment with the necessary dependencies. Follow these steps to get started:

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Quick Install

1. **Clone the Repository**

   Clone the game repository from the source:

   ```bash
   git clone <repository-url>
   cd tower-of-the-sorcerer
   ```

2. **Install Dependencies**

   Use pip to install the required dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `pygame` library, which is essential for running the game.

## Game Features

- **Map Size:** The game map is 80x80 tiles, providing a vast dungeon to explore.
- **Player Movement:** Control the player character using the keyboard keys W (up), S (down), A (left), and D (right).
- **Interactive Elements:**
  - **Monsters:** Engage in combat where your HP is compared to the monster's HP.
  - **Treasure Chests:** Restore 20-30 HP upon interaction.
  - **Walls:** Impassable obstacles that require strategic navigation.
  - **Doors:** Reach the door to progress to the next level.
- **Pathfinding:** There is always at least one path from the starting position to the door.

## How to Play

1. **Start the Game**

   Run the main game file:

   ```bash
   python main.py
   ```

2. **Game Controls**

   - Use `W` to move up.
   - Use `S` to move down.
   - Use `A` to move left.
   - Use `D` to move right.

3. **Objective**

   Navigate through the dungeon, avoid or defeat monsters, collect treasures to restore HP, and find the door to advance to the next level.

4. **Game Mechanics**

   - **Health Management:** Keep an eye on your HP. Interact with treasure chests to restore health.
   - **Combat:** Your HP will decrease when encountering monsters. Plan your moves to minimize damage.
   - **Exploration:** Explore the map to find the optimal path to the door while collecting treasures.

## Troubleshooting

- **Game Not Starting:** Ensure all dependencies are installed correctly. Check for any error messages in the terminal.
- **Controls Not Responding:** Make sure the game window is active and focused when using the keyboard controls.
- **Graphical Issues:** Verify that your system supports `pygame` and that your graphics drivers are up to date.

For further assistance, please contact our support team or refer to the game's documentation for more detailed troubleshooting steps.

Enjoy your adventure in the "Tower of the Sorcerer"!